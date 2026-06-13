import sys
from pathlib import Path

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).parent
sys.path.append(str(PROJECT_ROOT / "src"))

from pangya_physics.club import CLUBS
from pangya_physics.wind import Wind
from pangya_physics.ball import Ball
from pangya_physics.vector import Vector3D
from pangya_physics.simulator import PangyaSimulator, STEP_TIME
from pangya_physics.solver import find_power, create_initial_velocity


st.set_page_config(
    page_title="PangYa Shot Physics",
    layout="wide",
)


def create_ball(club_info, power_percent):
    velocity = create_initial_velocity(
        club=club_info,
        power_percent=power_percent,
    )

    return Ball(
        position=Vector3D(0.0, 0.0, 0.0),
        velocity=velocity,
        rotation_spin=0.0,
        rotation_curve=0.0,
    )


def simulate_trajectory(club_name, target_distance, wind, max_steps=1000):
    club_info = CLUBS[club_name]

    power_result = find_power(
        club=club_info,
        wind=wind,
        target_distance=target_distance,
        target_height=0.0,
    )

    ball = create_ball(
        club_info=club_info,
        power_percent=power_result.power_percent,
    )

    simulator = PangyaSimulator(
        ball=ball,
        club=club_info,
        wind=wind,
    )

    trajectory = []

    for step in range(max_steps):
        ball = simulator.step(STEP_TIME)

        trajectory.append({
            "step": step,
            "time": step * STEP_TIME,
            "x": ball.position.x,
            "y": ball.position.y,
            "z": ball.position.z,
        })

        if ball.position.y <= 0 and step > 0:
            break

    df = pd.DataFrame(trajectory)

    summary = {
        "power_percent": power_result.power_percent * 100,
        "final_distance": power_result.final_distance,
        "error": power_result.error,
        "found": power_result.found,
        "reachable": power_result.reachable,
        "iterations": power_result.iterations,
        "max_height": df["y"].max(),
        "flight_time": df["time"].max(),
        "lateral_deviation": df["z"].iloc[-1],
    }

    return df, summary


st.title("PangYa Shot Physics")
st.markdown("Simulador físico e solver de potência baseado em engenharia reversa da Smart Calculator.")

with st.sidebar:
    st.header("Parâmetros")

    club_name = st.selectbox(
        "Taco",
        list(CLUBS.keys()),
        index=0,
    )

    target_distance = st.slider(
        "Distância alvo (yards)",
        min_value=30,
        max_value=350,
        value=200,
        step=5,
    )

    wind_speed = st.number_input(
        "Vento - velocidade",
        min_value=0.0,
        max_value=30.0,
        value=0.0,
        step=1.0,
    )

    wind_angle = st.number_input(
        "Vento - ângulo",
        min_value=0.0,
        max_value=360.0,
        value=0.0,
        step=5.0,
    )

wind = Wind(wind_speed, wind_angle)

df_traj, summary = simulate_trajectory(
    club_name=club_name,
    target_distance=target_distance,
    wind=wind,
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Power necessário", f"{summary['power_percent']:.2f}%")
col2.metric("Distância final", f"{summary['final_distance']:.2f} yd")
col3.metric("Erro", f"{summary['error']:.3f} yd")
col4.metric("Altura máxima", f"{summary['max_height']:.2f}")

col5, col6, col7 = st.columns(3)

col5.metric("Tempo de voo", f"{summary['flight_time']:.2f}s")
col6.metric("Iterações", summary["iterations"])
col7.metric("Alcançável", "Sim" if summary["reachable"] else "Não")

st.subheader("Trajetória do chute")

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(
    df_traj["x"],
    df_traj["y"],
    linewidth=2,
)

ax.set_title(f"Trajetória - {club_name} para {target_distance} yd")
ax.set_xlabel("Distância (yards)")
ax.set_ylabel("Altura")
ax.grid(True)

st.pyplot(fig)

st.subheader("Dados da trajetória")

st.dataframe(df_traj)
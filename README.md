# PangYa Shot Physics

Projeto de engenharia reversa, simulação física e análise de dados baseado na Smart Calculator de Acrisio para PangYa.

## Objetivo

O objetivo deste projeto não é simplesmente reproduzir a Smart Calculator original.

A proposta é:

- compreender e documentar o modelo físico do PangYa;
- reimplementar gradualmente o simulador em Python;
- validar resultados contra a Smart Calc original;
- criar análises de sensibilidade;
- desenvolver visualizações interativas;
- construir um portfólio de Analytics e Simulação.

---

## Motivação

PangYa foi um dos principais responsáveis pelo meu interesse em Excel, modelagem matemática e análise de sistemas.

Durante muitos anos a comunidade criou tabelas, planilhas e modelos empíricos para prever tacadas.

Posteriormente, Acrisio realizou engenharia reversa do jogo e desenvolveu a Smart Calculator, permitindo simulações muito mais próximas do comportamento real do PangYa.

Este projeto busca transformar esse conhecimento em um estudo moderno de:

- Python
- Simulação Física
- Data Analytics
- Visualização de Dados
- Engenharia Reversa

---

## Tecnologias

- Python
- NumPy
- Pandas
- Matplotlib
- Jupyter Notebook
- Pytest
- Git
- GitHub

Futuras tecnologias:

- Plotly
- Streamlit
- Docker

---

## Estrutura do Projeto

```text
pangya-shot-physics/
│
├── notebooks/
├── docs/
├── src/
│   └── pangya_physics/
├── tests/
├── data/
└── app/
```

---

## Componentes Implementados

### Vector3D

Responsável por:

- soma vetorial
- subtração
- normalização
- produto vetorial
- magnitude

---

### Ball

Representa o estado físico da bola.

Inclui:

- posição
- velocidade
- spin
- curva
- rotações
- massa
- altura máxima

---

### Club

Modela os tacos do PangYa.

Atualmente:

- Woods
- Irons
- Wedges

Propriedades:

- power_factor
- power_base
- loft (degree)
- rotation_spin
- rotation_curve

---

### Wind

Conversão de:

- intensidade
- direção

para vetores tridimensionais.

---

### Simulator

Primeira versão do motor físico.

Atualmente implementa:

- gravidade
- vento
- curva
- spin
- resistência do ar (drag)

---

### Solver

Primeira implementação de busca iterativa.

Objetivo:

Encontrar a velocidade necessária para atingir uma distância-alvo.

Esta implementação será substituída futuramente por uma versão inspirada na função original `find_power()` da Smart Calc.

---

## Análises Desenvolvidas

### Club Analysis

Análise dos tacos:

- Power Factor
- Power Base
- Rotation Spin
- Rotation Curve
- Loft

Notebook:

```text
02_club_analysis.ipynb
```

---

### Basic Trajectory

Primeiras simulações de trajetória.

Notebook:

```text
03_basic_trajectory.ipynb
```

---

### Sensitivity Analysis

Comparação de cenários:

- sem vento
- vento frontal
- vento traseiro
- vento lateral
- spin
- curva

Notebook:

```text
04_sensitivity_analysis.ipynb
```

---

### Distance Solver

Busca de velocidade para distância-alvo.

Notebook:

```text
05_distance_solver.ipynb
```

---

### Solver Grid Analysis

Avaliação do solver para múltiplas distâncias.

Notebook:

```text
06_solver_grid_analysis.ipynb
```

---

### Club Solver Comparison

Comparação entre tacos.

Notebook:

```text
07_club_solver_comparison.ipynb
```

---

## Roadmap

### Fase 1

- [x] Estrutura do projeto
- [x] Vetores 3D
- [x] Ball
- [x] Club
- [x] Wind
- [x] Simulator básico
- [x] Testes unitários

### Fase 2

- [x] Solver inicial
- [x] Club Analysis
- [x] Trajetórias básicas
- [x] Sensitivity Analysis

### Fase 3

- [ ] Portar initShot()
- [ ] Portar getSlope()
- [ ] Portar getValuesDegree()

### Fase 4

- [ ] Portar find_power()
- [ ] Dataset de validação
- [ ] Comparação Python vs Smart Calc

### Fase 5

- [ ] Dashboard Streamlit
- [ ] Visualização 3D
- [ ] Deploy

---

## Diferencial do Projeto

A Smart Calculator original é uma ferramenta para uso no jogo.

Este projeto tem outro foco:

| Smart Calc | PangYa Shot Physics |
|------------|---------------------|
| Calculadora | Projeto Analítico |
| JavaScript | Python |
| Foco em jogar | Foco em entender |
| Resultado direto | Documentação e validação |
| Ferramenta | Portfólio de Dados |

---

## Autor

Felipe Augusto Allage

Projeto desenvolvido para aprofundamento em:

- Python
- Simulação
- Data Analytics
- Engenharia Reversa
- Visualização de Dados
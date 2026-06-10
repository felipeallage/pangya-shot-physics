from pangya_physics import CLUBS, Wind, find_power

club = CLUBS["1W"]

result = find_power(
    club=club,
    wind=Wind(speed=0, degree=0),
    target_distance=250,
    target_height=0,
)

print(result)
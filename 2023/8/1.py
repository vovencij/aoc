import re
import math

file = open("input.txt")
instructions = file.readline().strip()
file.readline()
desert_map = {}
for line in file:
    # PBN = (JRP, RVT)
    node = re.search(r"(...) = \((...), (...)\)", line)
    desert_map[node.group(1)] = (node.group(2), node.group(3))

steps = 0
current_step = "AAA"
while current_step != "ZZZ":
    instruction = instructions[steps % len(instructions)]
    steps += 1
    current_step = desert_map[current_step][0] if instruction == 'L' else desert_map[current_step][1]

print(f"1. Steps from AAA to ZZZ: {steps}")
print("=======================")

current_steps = []
for key in desert_map.keys():
    if key[2] == 'A':
        current_steps.append(key)

steps = [0] * len(current_steps)
print(f"2. Starting steps {current_steps}")
for i in range(0, len(current_steps)):
    while not current_steps[i].endswith("Z"):
        instruction = instructions[steps[i] % len(instructions)]
        steps[i] += 1
        current_steps[i] = desert_map[current_steps[i]][0] if instruction == 'L' else desert_map[current_steps[i]][1]

    print(f"{steps} steps, to reach {current_steps}")

print(f"2. Steps to {current_steps}: {steps} -> {math.lcm(*steps)}")

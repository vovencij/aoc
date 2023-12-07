# https://adventofcode.com/2023/day/4

file = open("input.txt")
file_lines = file.read().splitlines()

points = []
for line in file_lines:
    scores = line[10::].split("|")

    winning_numbers = [int(v.strip()) for v in scores[0].strip().replace("  ", " ").split(" ")]
    numbers_we_have = [int(v.strip()) for v in scores[1].strip().replace("  ", " ").split(" ")]
    common_numbers = set(winning_numbers).intersection(set(numbers_we_have))
    points.append(len(common_numbers))

multipliers = [1 for i in range(0, len(points))]
# multipliers[0] = 1

for i in range(0, len(points)):
    if multipliers[i] == 0:
        print("Reached zero card multiplier")
        break

    for j in range(i + 1, i + points[i] + 1):
        multipliers[j] += multipliers[i]

    print(f"i: {i}, Multiplier: {multipliers[i]}, points: {points[i]}: Multipliers: {multipliers}")

print(f"Total points: {sum(points)} ({points})")
print(f"Multipliers: {multipliers}")
print(f"Total cards: {sum(multipliers)}")

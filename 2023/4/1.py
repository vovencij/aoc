# https://adventofcode.com/2023/day/4

file = open("input.txt")
file_lines = file.read().splitlines()

total_points = 0
for line in file_lines:
    scores = line[10::].split("|")

    winning_numbers = [int(v.strip()) for v in scores[0].strip().replace("  ", " ").split(" ")]
    numbers_we_have = [int(v.strip()) for v in scores[1].strip().replace("  ", " ").split(" ")]
    common_numbers = set(winning_numbers).intersection(set(numbers_we_have))
    if len(common_numbers) > 0:
        winning_points = 2 ** (len(common_numbers) - 1)
        total_points += winning_points
        print(f"{common_numbers} >> {winning_points}")

    print(winning_numbers)
    print(numbers_we_have)

print(f"Total points: {total_points}")

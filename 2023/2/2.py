# https://adventofcode.com/2023/day/2#part2
file = open("input.txt")
lines = file.readlines()

sumOfPowers = 0

# Game 1: 12 blue; 2 green, 13 blue, 19 red; 13 red, 3 green, 14 blue
for line in lines:
    game = line[5::].split(":")
    gameId = int(game[0])

    minCubes = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    gameResults = game[1].split(";")
    for gameResult in gameResults:
        oneGame = gameResult.strip().split(",")
        for gameCube in oneGame:
            cube = gameCube.strip().split(" ")
            cube_count = int(cube[0])
            cube_color = cube[1]
            minCubes[cube_color] = max(cube_count, minCubes[cube_color])

    power = 1
    for val in minCubes.values():
        print(val)
        power *= int(val)

    sumOfPowers += power

print(f"Sum of powers for games: {sumOfPowers}")

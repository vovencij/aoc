# https://adventofcode.com/2023/day/2
file = open("input.txt")
lines = file.readlines()

possibleGameIdsSum = 0

# Game 1: 12 blue; 2 green, 13 blue, 19 red; 13 red, 3 green, 14 blue
for line in lines:
    game = line[5::].split(":")
    gameId = int(game[0])

    initialCubes = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    impossible = False
    gameResults = game[1].split(";")
    for gameResult in gameResults:
        oneGame = gameResult.strip().split(",")
        for gameCube in oneGame:
            cube = gameCube.strip().split(" ")
            cube_count = int(cube[0])
            cube_color = cube[1]
            if initialCubes[cube_color] < cube_count:
                impossible = True
                break
        if impossible:
            break

    if impossible:
        print(f"Impossible: {line}")
    else:
        possibleGameIdsSum += gameId

print(f"Sum of possible game Ids: {possibleGameIdsSum}")

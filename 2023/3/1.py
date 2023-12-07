# https://adventofcode.com/2023/day/3

def read_matrix():
    file = open("input.txt")
    file_lines = file.read().splitlines()

    line_of_dots = "." * len(file_lines[0])
    res = [line_of_dots]
    res.extend(file_lines)
    res.append(line_of_dots)

    return res


def add_char(chars_around, ch):
    chars_around.add(ch)


lines = read_matrix()
width = len(lines[0])
digitsFound = 0
numbersFound = 0
sumOfAllNumbers = 0
for curLine in range(1, len(lines) - 1):
    curCol = 0
    ongoingNumber = ""
    charsAround = set()
    numberDone = False
    while curCol < width:
        curSymbol = lines[curLine][curCol]
        if curSymbol.isdigit():
            digitsFound += 1
            if ongoingNumber == "" and curCol > 0:
                add_char(charsAround, lines[curLine-1][curCol-1])
                add_char(charsAround, lines[curLine][curCol-1])
                add_char(charsAround, lines[curLine+1][curCol-1])
            ongoingNumber += curSymbol
            add_char(charsAround, lines[curLine-1][curCol])
            add_char(charsAround, lines[curLine+1][curCol])
            if curCol == width - 1:
                numberDone = True
        else:
            if ongoingNumber != "":
                if curCol < width - 1:
                    add_char(charsAround, lines[curLine-1][curCol])
                    add_char(charsAround, lines[curLine][curCol])
                    add_char(charsAround, lines[curLine+1][curCol])
                numberDone = True

        if numberDone:
            if len(charsAround) == 1:
                print(f"{curLine}: Only one char around {ongoingNumber}: {charsAround}, skipping")
            else:
                print(f"{curLine}: {ongoingNumber}")
                numbersFound += 1
                sumOfAllNumbers += int(ongoingNumber)

            ongoingNumber = ""
            charsAround = set()
            numberDone = False

        curCol += 1

print(f"digits: {digitsFound}, numbers: {numbersFound}, sum of all numbers: {sumOfAllNumbers}")


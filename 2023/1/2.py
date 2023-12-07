stringDigits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def starts_with_string_digit(input_string):
    for digit in stringDigits.keys():
        if str(input_string).startswith(digit):
            return stringDigits[digit]

    return None


file = open("input.txt")
lines = file.readlines()
sumOfNums = 0
for line in lines:
    firstDigit = "0"
    for i in range(len(line)):
        if line[i].isdigit():
            firstDigit = line[i]
            break

        firstStringDigit = starts_with_string_digit(line[i::])
        if firstStringDigit is not None:
            firstDigit = firstStringDigit
            break

    lastDigit = "0"
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            lastDigit = line[i]
            break

        lastStringDigit = starts_with_string_digit(line[i::])
        if lastStringDigit is not None:
            lastDigit = lastStringDigit
            break

    num = int(f"{firstDigit}{lastDigit}")
    print(f"{line} -> {num}")
    sumOfNums += num

print(sumOfNums)

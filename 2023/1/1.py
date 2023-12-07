file = open("input.txt")
lines = file.readlines()
sumOfNums = 0
for line in lines:
    firstDigit = "0"
    lastDigit = "0"
    for c in line:
        if c.isdigit():
            firstDigit = c
            break

    for c in line[::-1]:
        if c.isdigit():
            lastDigit = c
            break

    num = int(f"{firstDigit}{lastDigit}")
    print(f"{line} -> {num}")
    sumOfNums += num

print(sumOfNums)

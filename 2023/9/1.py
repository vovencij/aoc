def calculate_diffs(row):
    res = []
    for i in range(1, len(row)):
        res.append(row[i] - row[i-1])
    return res


def all_zeros(row):
    for n in row:
        if n != 0:
            return False
    return True


def extrapolate_last(rows):
    res = 0
    for i in range(len(rows)-2, -1, -1):
        cur_row = rows[i]
        s = f"{i} {cur_row} + {res} -> "
        res = cur_row[-1] + res
        print(f"{s} {res}")
    return res


def extrapolate_first(rows):
    res = 0
    for i in range(len(rows)-2, -1, -1):
        cur_row = rows[i]
        s = f"{i} {cur_row} + {res} -> "
        res = cur_row[0] - res
        print(f"{s} {res}")
    return res


_input = open("input.txt")
lines = _input.readlines()
# lines = ["0 3 6 9 12 15",
#          "1 3 6 10 15 21",
#          "10 13 16 21 30 45"]
last_extra_sum = 0
first_extra_sum = 0
for line in lines:
    start_row = []
    for nr in line.strip().split(" "):
        start_row.append(int(nr))

    diffs = [start_row]
    diff = calculate_diffs(start_row)
    diffs.append(diff)
    while not all_zeros(diff):
        diff = calculate_diffs(diff)
        diffs.append(diff)

    print(f"{start_row}")
    print(f"{diffs}")
    last = extrapolate_last(diffs)
    last_extra_sum += last
    first = extrapolate_first(diffs)
    first_extra_sum += first
    print(f"Extrapolated first: {first}, last: {last}")
    print("===========")

print(f"Sum of first extrapolations: {first_extra_sum}")
print(f"Sum of last extrapolations: {last_extra_sum}")

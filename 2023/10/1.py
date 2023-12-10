def find_start(__map):
    for start_y in range(0, len(_map)):
        for start_x in range(0, len(_map[start_y])):
            if _map[start_y][start_x] == "S":
                return start_y, start_x
    return -1, -1


def next_move(_map, prev_line, prev_col, cur_line, cur_col):
    if cur_line == prev_line and cur_col == prev_col:
        print("Error, prev == cur in next_move")
        exit(1)

    cur_tile = _map[cur_line][cur_col]
    if cur_tile == "|":
        if prev_line < cur_line:
            return cur_line + 1, cur_col
        else:
            return cur_line - 1, cur_col
    elif cur_tile == "-":
        if prev_col < cur_col:
            return cur_line, cur_col + 1
        else:
            return cur_line, cur_col - 1
    elif cur_tile == "L":  # north-east
        if prev_line < cur_line:
            return cur_line, cur_col + 1
        else:
            return cur_line - 1, cur_col
    elif cur_tile == "J":  # north-west
        if prev_line < cur_line:
            return cur_line, cur_col - 1
        else:
            return cur_line - 1, cur_col
    elif cur_tile == "7":  # south-west
        if prev_line > cur_line:
            return cur_line, cur_col - 1
        else:
            return cur_line + 1, cur_col
    elif cur_tile == "F":  # south-east
        if prev_line > cur_line:
            return cur_line, cur_col + 1
        else:
            return cur_line + 1, cur_col

    print("Next move failed!")
    return -1, -1


def clean_the_loop(_map, _loop):
    for _l in range(0, len(_map)):
        _line = list(_map[_l])
        for _c in range(0, len(_line)):
            if (_l, _c) not in _loop:
                _line[_c] = "."
        _map[_l] = "".join(_line)


def count_intersections(_map, _line, _col):
    print(f"Checking at {_line}:{_col}")
    res = 0
    prev = None
    for _i in range(_col + 1, len(_map[_line])):
        cur = _map[_line][_i]
        if cur == "|":
            res += 1
        elif cur == "L":
            if prev is None:
                prev = "L"
                res += 1
            else:
                print(f"1. Unexpected char after {prev} at {_line},{_i}: {cur}")
                exit(1)
        elif cur == "7":
            if prev is None:
                print(f"2. Unexpected {cur} at {_line},{_i}")
                exit(1)
            elif prev == "L":
                prev = None
            elif prev == "F":
                res += 1
                prev = None
            else:
                print(f"3. Unexpected char before {cur} at {_line},{_i}: {prev}")
                exit(1)
        elif cur == "J":
            if prev is None:
                print(f"4. Unexpected {cur} at {_line},{_i}")
                exit(1)
            elif prev == "F":
                prev = None
            elif prev == "L":
                res += 1
                prev = None
            else:
                print(f"5. Unexpected char before {cur} at {_line},{_i}: {prev}")
                exit(1)
        elif cur == "F":
            if prev is None:
                prev = "F"
                res += 1
            else:
                print(f"6. Unexpected char after {prev} at {_line},{_i}: {cur}")
                exit(1)
    return res


def fix_start(_map, start_l, start_c, first_l, first_c, second_l, second_c):
    lll = list(_map[start_l])

    if first_l == second_l:
        start_tile = "-"
    elif first_c == second_c:
        start_tile = "|"
    elif (first_c == start_c and first_l == start_l - 1 and second_c == start_c + 1 and second_l == start_l)\
            or (second_c == start_c and second_l == start_l - 1 and first_c == start_c + 1 and first_l == start_l):
        start_tile = "L"
    elif (first_c == start_c - 1 and first_l == start_l and second_c == start_c and second_l == start_l - 1)\
            or (second_c == start_c - 1 and second_l == start_l and first_c == start_c and first_l == start_l - 1):
        start_tile = "J"
    elif (first_c == start_c - 1 and first_l == start_l and second_c == start_c and second_l == start_l + 1)\
            or (second_c == start_c - 1 and second_l == start_l and first_c == start_c and first_l == start_l + 1):
        start_tile = "7"
    elif (first_c == start_c and first_l == start_l + 1 and second_c == start_c + 1 and second_l == start_l)\
            or (second_c == start_c and second_l == start_l + 1 and first_c == start_c + 1 and first_l == start_l):
        start_tile = "F"
    else:
        print("failed to adjust start")
        print(f"first: ({first_l}:{first_c}) {_map[first_l][first_c]}")
        print(f"start: ({start_l}:{start_c}) {_map[start_l][start_c]}")
        print(f"second: ({second_l}:{second_c}) {_map[second_l][second_c]}")
        exit(1)

    lll[start_c] = start_tile
    _map[start_l] = "".join(lll)


file = open("input.txt")
_map = file.read().splitlines()
start = find_start(_map)

print(start)

start_line = start[0]
start_col = start[1]
first_end_line = None
first_end_col = None
second_end_line = None
second_end_col = None
loop = set()

if start_line > 0 and _map[start_line - 1][start_col] in "|7F":
    if first_end_line is None:
        first_end_line = start_line - 1
        first_end_col = start_col
    elif second_end_line is None:
        second_end_line = start_line - 1
        second_end_col = start_col
    else:
        print("Error 1!")
if start_col > 0 and _map[start_line][start_col - 1] in "-LF":
    if first_end_line is None:
        first_end_line = start_line
        first_end_col = start_col - 1
    elif second_end_line is None:
        second_end_line = start_line
        second_end_col = start_col - 1
    else:
        print("Error 2!")

if start_col < len(_map[0]) - 1 and _map[start_line][start_col + 1] in "-J7":
    if first_end_line is None:
        first_end_line = start_line
        first_end_col = start_col + 1
    elif second_end_line is None:
        second_end_line = start_line
        second_end_col = start_col + 1
    else:
        print("Error 3!")

if start_line < len(_map) - 1 and _map[start_line + 1][start_col] in "|LJ":
    if first_end_line is None:
        first_end_line = start_line + 1
        first_end_col = start_col
    elif second_end_line is None:
        second_end_line = start_line + 1
        second_end_col = start_col
    else:
        print("Error 4!")

if first_end_line is None or second_end_line is None:
    print("Failed to find first moves")
else:
    print(f"First moves: {_map[first_end_line][first_end_col]}({first_end_line}:{first_end_col}) and {_map[second_end_line][second_end_col]}({second_end_line}:{second_end_col})")

prev_first_line = start_line
prev_first_col = start_col
prev_second_line = start_line
prev_second_col = start_col
loop.add((start_line, start_col))
loop.add((first_end_line, first_end_col))
loop.add((second_end_line, second_end_col))
fix_start(_map, start_line, start_col, first_end_line, first_end_col, second_end_line, second_end_col)

i = 1
while first_end_col != second_end_col or first_end_line != second_end_line:
    i += 1
    (next_first_line, next_first_col) = next_move(_map, prev_first_line, prev_first_col, first_end_line, first_end_col)
    (prev_first_line, prev_first_col) = (first_end_line, first_end_col)
    (first_end_line, first_end_col) = (next_first_line, next_first_col)

    (next_second_line, next_second_col) = next_move(_map, prev_second_line, prev_second_col, second_end_line, second_end_col)
    (prev_second_line, prev_second_col) = (second_end_line, second_end_col)
    (second_end_line, second_end_col) = (next_second_line, next_second_col)

    loop.add((first_end_line, first_end_col))
    loop.add((second_end_line, second_end_col))

print(f"Task 1: Max loop distance: {i}")
clean_the_loop(_map, loop)
fout = open("output.txt", mode="w")
for l in _map:
    fout.write(l)
    fout.write("\n")
fout.close()

in_the_loop = 0
for line in range(1, len(_map) - 1):
    for col in range(1, len(_map[0]) - 1):
        if _map[line][col] == ".":
            intersection = count_intersections(_map, line, col)
            # https://en.wikipedia.org/wiki/Point_in_polygon
            in_the_loop += intersection % 2

print(f"Task 2: Tiles in the loop: {in_the_loop}")

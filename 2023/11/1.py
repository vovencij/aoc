

def read_and_expand_universe(_f):
    ff = open(_f)
    line = ff.readline()
    res = []

    vertical_expansion_indices = []
    i = 0
    while line:
        line = line.strip()
        res.append(line)
        if line.find("#") == -1:
            vertical_expansion_indices.append(i)
        line = ff.readline()
        i += 1
    ff.close()

    horizontal_expansion_indices = []
    for c in range(0, len(res[0])):
        all_dots_in_column = True
        for _l in range(0, len(res)):
            if res[_l][c] == "#":
                all_dots_in_column = False
                break
        if all_dots_in_column:
            horizontal_expansion_indices.append(c)

    return res, vertical_expansion_indices, horizontal_expansion_indices


def find_pairs(_universe):
    pairs = []
    for _line_from in range(0, len(_universe)):
        for _col_from in range(0, len(_universe[_line_from])):
            if _universe[_line_from][_col_from] == "#":
                # First, scan the same line to the end
                for i in range(_col_from + 1, len(_universe[_line_from])):
                    if _universe[_line_from][i] == "#":
                        pairs.append((_line_from, _col_from, _line_from, i))

                # Next, scan full lines starting from next line
                for _line_to in range(_line_from + 1, len(_universe)):
                    for _col_to in range(0, len(_universe[_line_to])):
                        if _universe[_line_to][_col_to] == "#":
                            pairs.append((_line_from, _col_from, _line_to, _col_to))

    return pairs


# _pair_of_coordinates: (line_from, column_from, line_to, column_from)
def calculate_distance(_pair_of_coordinates, vertical_expansion_indices, horizontal_expansion_indices, expansion_count):
    from_line = min(_pair_of_coordinates[2], _pair_of_coordinates[0])
    to_line = max(_pair_of_coordinates[2], _pair_of_coordinates[0])
    from_col = min(_pair_of_coordinates[3], _pair_of_coordinates[1])
    to_col = max(_pair_of_coordinates[3], _pair_of_coordinates[1])
    distance = (to_line - from_line) + (to_col - from_col)
    total_expansion = 0
    for ve in vertical_expansion_indices:
        if from_line < ve < to_line:
            total_expansion += expansion_count
    for he in horizontal_expansion_indices:
        if from_col < he < to_col:
            total_expansion += expansion_count

    # print(f"Distance between {_pair_of_coordinates} is {distance}, total_expansion is {total_expansion}")
    return distance + total_expansion


universe = read_and_expand_universe("input.txt")
print(f"Vertical Expansion: {universe[1]}")
print(f"Horizontal Expansion: {universe[2]}")

expansion = 999999
pairs_of_stars = find_pairs(universe[0])
print(f"Found {len(pairs_of_stars)} pairs")
sum_of_distances = 0
for pair in pairs_of_stars:
    sum_of_distances += calculate_distance(pair, universe[1], universe[2], expansion)

print(f"Sum of distances = {sum_of_distances}")

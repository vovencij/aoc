import time


DEBUG = False


def current_milli_time():
    return round(time.time() * 1000)


def get_arrangement(layout):
    cur_group = 0
    res = []
    for _i in range(0, 22):
        cur_mask = 2 ** _i
        cur = layout & cur_mask
        if cur > 0:
            cur_group += 1
        elif cur_group > 0:
            res.append(cur_group)
            cur_group = 0
    return res


def count_suitable_arrangements(line, multiplier):
    parts = line.strip().split(" ")
    pattern = parts[0]
    tmp_arr = parts[1]
    for i in range(1, multiplier):
        pattern += "?" + parts[0]
        tmp_arr += "," + parts[1]

    arrangement = [int(i) for i in tmp_arr.split(",")]
    arrangement.reverse()

    print(f"pattern: {pattern}, arrangement: {arrangement}")
    res = count_arrangements_2(pattern, arrangement)

    return res


def count_arrangements_2(pattern, arrangement):
    pattern_len = len(pattern)

    max_mask = (2**pattern_len) - 1
    broken_spring_mask = 0
    left_most_broken_spring = 0  # Optimization: We will start iterating starting with this, as we MUST have this left-most bit set for broken springs
    working_spring_mask = 0
    for i in range(0, pattern_len):
        flip_mask = 2**i
        if pattern[pattern_len - i - 1] == ".":
            working_spring_mask |= flip_mask
        elif pattern[pattern_len - i - 1] == "#":
            broken_spring_mask |= flip_mask
            left_most_broken_spring = flip_mask

    suitable_arrangements = 0
    for i in range(left_most_broken_spring, 2 ** pattern_len):
        working_mask_check = (i ^ max_mask) & working_spring_mask == working_spring_mask
        broken_mask_check = i & broken_spring_mask == broken_spring_mask
        if working_mask_check and broken_mask_check:
            cur_arr = get_arrangement(i)
            suitable = cur_arr == arrangement
            if DEBUG:
                print(f"{i:20b} {cur_arr} vs {arrangement} -> {suitable}")
            if suitable:
                suitable_arrangements += 1

    print(f"{pattern} ({pattern_len}), {arrangement}, max mask: {max_mask:b}, working_spring_mask: {working_spring_mask:b}, "
          f"broken_spring_mask: {broken_spring_mask:b}, suitable arrangements: {suitable_arrangements}")
    return suitable_arrangements


lines = open("input.txt").readlines()
# lines = ["?###???????? 3,2,1"]
total_suitable_arrangements = 0
total_times_5 = 0
for _line in lines:
    arrangements = count_suitable_arrangements(_line, 1)
    total_suitable_arrangements += arrangements


print(f"Suitable arrangements: {total_suitable_arrangements}, times 5: {total_times_5}")

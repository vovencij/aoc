import time


def current_milli_time():
    return round(time.time() * 1000)


def approach_one(time, current_record):
    winning_combos = 0
    for hold_time in range(0, time):
        potential_distance = hold_time * (time - hold_time)
        if potential_distance > current_record:
            winning_combos += 1

    print(f"Winning combos: {winning_combos}")
# Winning combos: 27102791


def approach_two(time, current_record):
    record_start = 0
    for hold_time in range(0, time):
        potential_distance = hold_time * (time - hold_time)
        if potential_distance > current_record:
            record_start = hold_time
            break

    record_end = 0
    for hold_time in range(time, 0, -1):
        potential_distance = hold_time * (time - hold_time)
        if potential_distance > current_record:
            record_end = hold_time
            break
    print(f"Winning combos: {record_end-record_start+1}")


lines = open("input.txt").readlines()

_time = int(lines[0].removeprefix("Time:").strip().replace(" ", ""))
_current_record = int(lines[1].removeprefix("Distance:").replace(" ", ""))

print(f"Checking time {_time}, record: {_current_record}")

t = current_milli_time()
approach_one(_time, _current_record)
t2 = current_milli_time()
print(f"Took {t2-t}ms")
approach_two(_time, _current_record)
t3 = current_milli_time()
print(f"Took {t3-t2}ms")


lines = open("input.txt").readlines()
# lines = ["Time:      7  15   30","Distance:  9  40  200"]

times = []
for x in lines[0].removeprefix("Time:").strip().split(" "):
    t = x.strip()
    if t != "":
        times.append(int(t))

distances = []
for x in lines[1].removeprefix("Distance:").strip().split(" "):
    d = x.strip()
    if d != "":
        distances.append(int(d))

total_winning_combos = 1
for i in range(0, len(times)):
    time = times[i]
    current_record = distances[i]

    print(f"Checking time {time}, record: {current_record}")
    winning_combos = 0
    for hold_time in range(0, time):
        potential_speed = hold_time
        potential_distance = potential_speed * (time - hold_time)
        if potential_distance > current_record:
            winning_combos += 1
            print(f"Hold time: {hold_time}, Speed: {potential_speed}, Distance: {potential_distance}")
    print(f"Winning combos: {winning_combos}")
    total_winning_combos *= winning_combos

print(f"Total winning combos: {total_winning_combos}")

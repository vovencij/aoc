from __future__ import annotations
import time


class Range:

    def __init__(self, _from, _to, is_adjusted=False):
        self._from = _from
        self._to = _to
        self.is_adjusted = is_adjusted

    def __repr__(self):
        return f"({self._from} : {self._to}){'*' if self.is_adjusted else ''}"

    def fully_outside(self, other_range: Range):
        return self._to < other_range._from or self._from > other_range._to

    def fully_inside(self, other_range: Range):
        return self._from >= other_range._from and self._to <= other_range._to

    def intersect_and_adjust(self, other_range: Range, adjustment=0):
        res = []
        working_from = self._from
        if working_from < other_range._from:
            res.append(Range(working_from, other_range._from - 1))
            working_from = other_range._from

        last_part = None
        working_to = self._to
        if working_to > other_range._to:
            last_part = Range(other_range._to + 1, working_to)
            working_to = other_range._to

        res.append(Range(working_from, working_to).adjust(adjustment))

        if last_part is not None:
            res.append(last_part)

        return res

    def adjust(self, adjustment):
        return Range(self._from + adjustment, self._to + adjustment, is_adjusted=True)

    def value_in_range(self, value):
        return self._from <= value <= self._to


class AlmanacEntry:

    def __init__(self, dest, src, a_range):
        self.src_range = Range(src, src + a_range - 1)
        self.dest_range = Range(dest, dest + a_range - 1)
        self.adjustment = dest - src

    def map_value(self, value):
        if self.src_range.value_in_range(value):
            return value + self.adjustment

        return None

    # range -> list of ranges
    def map_range(self, _range: Range):
        if _range.fully_outside(self.src_range):
            return [_range]
        if _range.fully_inside(self.src_range):
            return [_range.adjust(self.adjustment)]

        return _range.intersect_and_adjust(self.src_range, self.adjustment)


class Almanac:

    def __init__(self, name):
        self.entries = []
        _file = open("input.txt")
        file_lines = _file.read().splitlines()
        do_add = False
        for line in file_lines:
            if not do_add and line.find(name) >= 0:
                do_add = True
            elif do_add and line.strip() == "":
                break
            elif do_add:
                line_parts = line.split(" ")
                self.add_entry(int(line_parts[0]), int(line_parts[1]), int(line_parts[2]))

    def add_entry(self, dest, src, a_range):
        self.entries.append(AlmanacEntry(dest, src, a_range))

    def map_value(self, value):
        for _almanac in self.entries:
            res = _almanac.map_value(value)
            if res is not None:
                return res

        return value

    def map_range(self, _range: Range):
        adjusted_ranges = []
        unadjusted_ranges = [_range]
        for _almanac in self.entries:
            working_copy_of_unadjusted_ranges = unadjusted_ranges.copy()
            unadjusted_ranges.clear()
            for src_range in working_copy_of_unadjusted_ranges:
                modified_ranges = _almanac.map_range(src_range)
                for mod_range in modified_ranges:
                    if mod_range.is_adjusted:
                        adjusted_ranges.append(mod_range)
                    else:
                        unadjusted_ranges.append(mod_range)

        res = adjusted_ranges + unadjusted_ranges
        for r in res:
            r.is_adjusted = False

        return res

    def map_ranges(self, _ranges):
        res = []
        for _r in _ranges:
            res.extend(self.map_range(_r))
        return res


class AlmanacChain:

    def __init__(self):
        self.seed_to_soil = Almanac("seed-to-soil")
        self.soil_to_fertilizer = Almanac("soil-to-fertilizer")
        self.fertilizer_to_water = Almanac("fertilizer-to-water")
        self.water_to_light = Almanac("water-to-light")
        self.light_to_temperature = Almanac("light-to-temperature")
        self.temperature_to_humidity = Almanac("temperature-to-humidity")
        self.humidity_to_location = Almanac("humidity-to-location")

    def seed_to_location(self, seed):
        soil = self.seed_to_soil.map_value(seed)
        fertilizer = self.soil_to_fertilizer.map_value(soil)
        water = self.fertilizer_to_water.map_value(fertilizer)
        light = self.water_to_light.map_value(water)
        temp = self.light_to_temperature.map_value(light)
        humidity = self.temperature_to_humidity.map_value(temp)
        return self.humidity_to_location.map_value(humidity)

    def seed_range_to_location_ranges(self, seed_range):
        soils = self.seed_to_soil.map_range(seed_range)
        fertilizers = self.soil_to_fertilizer.map_ranges(soils)
        waters = self.fertilizer_to_water.map_ranges(fertilizers)
        lights = self.water_to_light.map_ranges(waters)
        temps = self.light_to_temperature.map_ranges(lights)
        humidities = self.temperature_to_humidity.map_ranges(temps)
        return self.humidity_to_location.map_ranges(humidities)


def task_one(seeds):
    min_loc = None
    for seed in seeds:
        loc = almanac.seed_to_location(int(seed))
        if min_loc is None:
            min_loc = loc
        else:
            min_loc = min(min_loc, loc)
        print(f"{seed} -> {loc}")

    return min_loc


def task_two(seeds):
    min_loc = None
    for i in range(0, len(seeds) - 1, 2):
        print(f"{seeds[i]} : {seeds[i + 1]} -> ")
        start = int(seeds[i])
        end = start + int(seeds[i + 1]) - 1

        s_range = Range(start, end)
        location_ranges = almanac.seed_range_to_location_ranges(s_range)
        for loc_ran in location_ranges:
            min_loc = loc_ran._from if min_loc is None else min(min_loc, loc_ran._from)
        print(f"    {location_ranges}")
    print(f"min_loc: {min_loc}")


def current_milli_time():
    return round(time.time() * 1000)


t = current_milli_time()
almanac = AlmanacChain()
file = open("input.txt")
_seeds = file.read().splitlines()[0].removeprefix("seeds: ").split(" ")
# task_one(_seeds)
# print("==========================")
task_two(_seeds)
elapsed_time = current_milli_time() - t
print(f"Elapsed time: {elapsed_time}")
# seed_range = Range(3, 14)
# mapping_range = Range(5, 10)
# if seed_range.fully_inside(mapping_range):
#     print("seed range is fully inside mapping range")
# elif seed_range.fully_outside(mapping_range):
#     print("seed range is fully outside mapping range")
# else:
#     print(f"seed range intersects with mapping range: {seed_range.intersect_and_adjust(mapping_range, 100)}")

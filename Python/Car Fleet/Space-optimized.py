# Car Fleet — Space-optimized (O(1) extra space)
# Sort by position descending (closest to target first). Track the max time seen.
# A new fleet forms whenever the current car's time > max_time; otherwise it merges.

def car_fleet_space_optimized(target, position, speed):
    cars = sorted(zip(position, speed), reverse=True)  # sort by position desc
    fleets = 0
    max_time = -1.0

    for p, v in cars:
        t = (target - p) / v
        if t > max_time + 1e-12:
            fleets += 1
            max_time = t  # this fleet becomes the new "barrier"
        # else: merges into the fleet with time max_time

    return fleets


# Quick tests
print("Space-optimized:")
print(car_fleet_space_optimized(10, [1, 4], [3, 2]))             # -> 1
print(car_fleet_space_optimized(10, [4, 1, 0, 7], [2, 2, 1, 1])) # -> 3

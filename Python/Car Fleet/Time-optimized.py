# Car Fleet — Time-optimized (linear) via counting buckets
# Since 0 <= position[i] < target and target <= 1000, we can bucket times by position.
# Iterate positions from target-1 down to 0 and apply the same "max time" rule.

def car_fleet_time_optimized(target, position, speed):
    # bucket[pos] = time to reach target for the car that starts at 'pos'
    bucket = [None] * target
    for p, v in zip(position, speed):
        bucket[p] = (target - p) / v

    fleets = 0
    max_time = -1.0
    for p in range(target - 1, -1, -1):  # from closest to target down to farthest
        t = bucket[p]
        if t is None:
            continue
        if t > max_time + 1e-12:
            fleets += 1
            max_time = t
        # else: merges

    return fleets


# Quick tests
print("Time-optimized:")
print(car_fleet_time_optimized(10, [1, 4], [3, 2]))             # -> 1
print(car_fleet_time_optimized(10, [4, 1, 0, 7], [2, 2, 1, 1])) # -> 3

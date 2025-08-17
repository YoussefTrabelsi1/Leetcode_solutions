# Car Fleet — Brute-force event simulation
# Idea: advance time to the next "event": either a catch-up between adjacent cars
# or an arrival at the destination. Merge fleets when positions coincide; remove
# fleets that reach target. Repeat until all cars are gone.

def car_fleet_bruteforce(target, position, speed):
    EPS = 1e-9
    # cars sorted by position (ascending)
    cars = [{'p': p, 'v': v} for p, v in sorted(zip(position, speed))]
    fleets_arrived = 0

    while cars:
        # find earliest event time
        dt = float('inf')
        # arrival events
        for c in cars:
            dt = min(dt, (target - c['p']) / c['v'])

        # catch events (only between adjacent cars)
        for i in range(len(cars) - 1):
            a, b = cars[i], cars[i + 1]
            if a['v'] > b['v']:
                tcatch = (b['p'] - a['p']) / (a['v'] - b['v'])
                catch_pos = a['p'] + a['v'] * tcatch
                if tcatch >= -EPS and catch_pos <= target + EPS:
                    dt = min(dt, tcatch)

        if dt == float('inf'):
            # no more catches before arrivals; remaining all arrive as-is
            fleets_arrived += len(cars)
            break

        # advance all cars by dt
        for c in cars:
            c['p'] = min(target, c['p'] + c['v'] * dt)

        # merge cars that are now at same position (adjacent equal p become one fleet)
        merged = []
        i = 0
        while i < len(cars):
            j = i
            while j + 1 < len(cars) and abs(cars[j + 1]['p'] - cars[i]['p']) <= EPS:
                j += 1
            # keep the foremost one in this block (same position), its speed dictates the fleet
            merged.append({'p': cars[j]['p'], 'v': cars[j]['v']})
            i = j + 1
        cars = merged  # still sorted by p

        # remove fleets that reached target (from the end, since list is ascending by p)
        while cars and abs(cars[-1]['p'] - target) <= EPS:
            fleets_arrived += 1
            cars.pop()

    return fleets_arrived


# Quick tests
print("Brute force:")
print(car_fleet_bruteforce(10, [1, 4], [3, 2]))             # -> 1
print(car_fleet_bruteforce(10, [4, 1, 0, 7], [2, 2, 1, 1])) # -> 3

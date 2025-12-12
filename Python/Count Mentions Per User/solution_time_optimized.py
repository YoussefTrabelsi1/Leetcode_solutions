# file: solution_time_optimized.py
from typing import List
import heapq

def count_mentions(numberOfUsers: int, events: List[List[str]]) -> List[int]:
    # Time-optimized:
    # - Avoid O(U) per HERE/ALL message via lazy counters
    #   ALL: count all_total, add to everyone at end
    #   HERE: count here_total, and for each user track here_offset for their online intervals
    #         settle (here_total - here_offset[user]) when they go offline / at end
    #
    # - Use a min-heap for auto-online events (time_to_return, user)
    mentions = [0] * numberOfUsers
    online = [True] * numberOfUsers

    all_total = 0
    here_total = 0
    here_offset = [0] * numberOfUsers  # valid when online: start-of-online-interval here_total

    # Sort events by timestamp; at same timestamp, we will process:
    # 1) auto-online (heap)
    # 2) OFFLINE
    # 3) MESSAGE
    buckets = {}
    for typ, ts, payload in events:
        t = int(ts)
        buckets.setdefault(t, []).append((typ, payload))

    return_heap = []  # (time, user)

    def apply_returns(up_to_time: int) -> None:
        nonlocal return_heap
        while return_heap and return_heap[0][0] <= up_to_time:
            rt, u = heapq.heappop(return_heap)
            if not online[u]:
                online[u] = True
                here_offset[u] = here_total  # start accruing HERE again from now

    for t in sorted(buckets.keys()):
        apply_returns(t)

        # OFFLINE before MESSAGE at same timestamp
        offs = [p for (typ, p) in buckets[t] if typ == "OFFLINE"]
        msgs = [p for (typ, p) in buckets[t] if typ == "MESSAGE"]

        for payload in offs:
            u = int(payload)
            # settle pending HERE contributions accrued while online (strictly before time t)
            mentions[u] += here_total - here_offset[u]
            online[u] = False
            heapq.heappush(return_heap, (t + 60, u))

        for s in msgs:
            if s == "ALL":
                all_total += 1
            elif s == "HERE":
                here_total += 1
            else:
                for tok in s.split():
                    u = int(tok[2:])
                    mentions[u] += 1

    # Apply any remaining HERE contributions for users still online
    for u in range(numberOfUsers):
        if online[u]:
            mentions[u] += here_total - here_offset[u]

    # Apply ALL contributions to everyone
    if all_total:
        for u in range(numberOfUsers):
            mentions[u] += all_total

    return mentions


if __name__ == "__main__":
    print(count_mentions(2, [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]))  # [2,2]
    print(count_mentions(2, [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]]))   # [2,2]
    print(count_mentions(2, [["OFFLINE","10","0"],["MESSAGE","12","HERE"]]))                              # [0,1]

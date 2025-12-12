# file: solution_bruteforce.py
from typing import List

def count_mentions(numberOfUsers: int, events: List[List[str]]) -> List[int]:
    # Brute force:
    # - Sort by (timestamp, OFFLINE before MESSAGE)
    # - Before each event, scan all users to auto-bring them online if needed
    # - For HERE / ALL, loop over all users and increment
    events_sorted = sorted(
        events,
        key=lambda e: (int(e[1]), 0 if e[0] == "OFFLINE" else 1)
    )

    mentions = [0] * numberOfUsers
    online = [True] * numberOfUsers
    back_time = [-1] * numberOfUsers  # if offline, time when becomes online again; else -1

    def refresh(cur_t: int) -> None:
        for u in range(numberOfUsers):
            if not online[u] and back_time[u] != -1 and back_time[u] <= cur_t:
                online[u] = True
                back_time[u] = -1

    for typ, ts, payload in events_sorted:
        t = int(ts)
        refresh(t)

        if typ == "OFFLINE":
            u = int(payload)
            online[u] = False
            back_time[u] = t + 60
        else:  # MESSAGE
            s = payload
            if s == "ALL":
                for u in range(numberOfUsers):
                    mentions[u] += 1
            elif s == "HERE":
                for u in range(numberOfUsers):
                    if online[u]:
                        mentions[u] += 1
            else:
                for tok in s.split():
                    # tok is like "id<number>"
                    u = int(tok[2:])
                    mentions[u] += 1

    return mentions


if __name__ == "__main__":
    print(count_mentions(2, [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]))  # [2,2]
    print(count_mentions(2, [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]]))   # [2,2]
    print(count_mentions(2, [["OFFLINE","10","0"],["MESSAGE","12","HERE"]]))                              # [0,1]

# file: solution_space_optimized.py
from typing import List

def count_mentions(numberOfUsers: int, events: List[List[str]]) -> List[int]:
    # Space-lean version:
    # - Only arrays (mentions, online, back_time)
    # - Group by timestamp, process:
    #   1) auto-online (scan users)
    #   2) OFFLINE events at this timestamp
    #   3) MESSAGE events at this timestamp
    mentions = [0] * numberOfUsers
    online = [True] * numberOfUsers
    back_time = [-1] * numberOfUsers

    # Group events by timestamp
    buckets = {}
    for typ, ts, payload in events:
        t = int(ts)
        buckets.setdefault(t, []).append((typ, payload))

    for t in sorted(buckets.keys()):
        # 1) auto-online before handling anything at time t
        for u in range(numberOfUsers):
            if not online[u] and back_time[u] != -1 and back_time[u] <= t:
                online[u] = True
                back_time[u] = -1

        # 2) OFFLINE before MESSAGE at the same timestamp
        offs = [p for (typ, p) in buckets[t] if typ == "OFFLINE"]
        msgs = [p for (typ, p) in buckets[t] if typ == "MESSAGE"]

        for payload in offs:
            u = int(payload)
            online[u] = False
            back_time[u] = t + 60

        for s in msgs:
            if s == "ALL":
                for u in range(numberOfUsers):
                    mentions[u] += 1
            elif s == "HERE":
                for u in range(numberOfUsers):
                    if online[u]:
                        mentions[u] += 1
            else:
                for tok in s.split():
                    u = int(tok[2:])
                    mentions[u] += 1

    return mentions


if __name__ == "__main__":
    print(count_mentions(2, [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]))  # [2,2]
    print(count_mentions(2, [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]]))   # [2,2]
    print(count_mentions(2, [["OFFLINE","10","0"],["MESSAGE","12","HERE"]]))                              # [0,1]

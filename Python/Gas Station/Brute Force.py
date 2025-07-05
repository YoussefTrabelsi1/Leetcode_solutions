from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        for i in range(n):
            tank = gas[i] - cost[i]
            if tank < 0:
                continue

            j = (i + 1) % n
            while j != i:
                tank += gas[j]
                tank -= cost[j]
                if tank < 0:
                    break
                j += 1
                j %= n

            if j == i:
                return i
        return -1
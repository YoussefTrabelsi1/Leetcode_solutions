from collections import deque
from typing import Counter


class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        q = deque()
        last_num, open_groups = -1, 0

        for num in sorted(count):
            if ((open_groups > 0 and num > last_num + 1) or 
                open_groups > count[num]
            ):
                return False

            q.append(count[num] - open_groups)
            last_num = num
            open_groups = count[num]

            if len(q) == groupSize:
                open_groups -= q.popleft()

        return open_groups == 0
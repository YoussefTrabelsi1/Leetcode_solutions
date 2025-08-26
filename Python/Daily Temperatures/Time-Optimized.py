from typing import List

def daily_temperatures_stack(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    result = [0] * n
    stack = []  # indices with decreasing temperatures
    for i, t in enumerate(temperatures):
        while stack and t > temperatures[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    return result

# Demo
if __name__ == "__main__":
    print(daily_temperatures_stack([30,38,30,36,35,40,28]))  # [1,4,1,2,1,0,0]
    print(daily_temperatures_stack([22,21,20]))              # [0,0,0]

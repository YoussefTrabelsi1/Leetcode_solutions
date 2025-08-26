from typing import List

def daily_temperatures_bruteforce(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    result = [0] * n
    for i in range(n - 1):
        for j in range(i + 1, n):
            if temperatures[j] > temperatures[i]:
                result[i] = j - i
                break
    return result

# Demo
if __name__ == "__main__":
    print(daily_temperatures_bruteforce([30,38,30,36,35,40,28]))  # [1,4,1,2,1,0,0]
    print(daily_temperatures_bruteforce([22,21,20]))              # [0,0,0]

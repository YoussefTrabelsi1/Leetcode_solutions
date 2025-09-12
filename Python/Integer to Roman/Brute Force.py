# Approach: Brute-force repeated subtraction.
# Keep subtracting the largest allowed Roman unit until the number reaches 0.
# This may append many symbols one-by-one (e.g., MMM for 3000).

def int_to_roman_bruteforce(num: int) -> str:
    # Full set including subtractive forms to obey constraints
    values  = [1000, 900, 500, 400, 100, 90,  50,  40,  10,  9,  5,  4,  1]
    symbols = ["M", "CM","D", "CD","C","XC","L","XL","X","IX","V","IV","I"]

    res = []
    i = 0
    # Repeated subtraction: may loop many times for large counts
    while num > 0:
        if num >= values[i]:
            res.append(symbols[i])
            num -= values[i]
        else:
            i += 1
    return "".join(res)

# ---- Quick tests ----
if __name__ == "__main__":
    for n in (3749, 58, 1994, 4, 9, 40, 90, 400, 900, 3999, 1):
        print(n, "->", int_to_roman_bruteforce(n))

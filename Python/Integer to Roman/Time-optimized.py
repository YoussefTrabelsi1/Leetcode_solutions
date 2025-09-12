# Approach: Time-optimized greedy.
# Iterate once over 13 (value, symbol) pairs; for each, compute count = num // value,
# append symbol * count, then num %= value. This minimizes iterations and string ops.

def int_to_roman_greedy(num: int) -> str:
    values  = (1000, 900, 500, 400, 100, 90,  50,  40,  10,  9,  5,  4,  1)
    symbols = ("M",  "CM","D", "CD","C","XC","L","XL","X","IX","V","IV","I")

    out = []
    for v, s in zip(values, symbols):
        if num == 0:
            break
        q, num = divmod(num, v)
        if q:
            out.append(s * q)
    return "".join(out)

# ---- Quick tests ----
if __name__ == "__main__":
    tests = {
        3749: "MMMDCCXLIX",
        58:   "LVIII",
        1994: "MCMXCIV",
        4:    "IV",
        9:    "IX",
        40:   "XL",
        90:   "XC",
        400:  "CD",
        900:  "CM",
        3999: "MMMCMXCIX",
        1:    "I",
    }
    for n, expected in tests.items():
        got = int_to_roman_greedy(n)
        print(n, "->", got, "| OK" if got == expected else f"| FAIL (expected {expected})")

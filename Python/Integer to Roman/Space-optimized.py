# Approach: Space-optimized lookup.
# Precompute minimal fixed lists for each decimal place:
# thousands (0-3), hundreds (0-9), tens (0-9), ones (0-9).
# Then build the Roman numeral with O(1) operations.

def int_to_roman_lookup(num: int) -> str:
    thousands = ["", "M", "MM", "MMM"]                  # 0..3
    hundreds  = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]  # 0..9
    tens      = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]  # 0..9
    ones      = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]  # 0..9

    t = thousands[num // 1000]
    h = hundreds[(num % 1000) // 100]
    te = tens[(num % 100) // 10]
    o = ones[num % 10]
    return t + h + te + o

# ---- Quick tests ----
if __name__ == "__main__":
    examples = [3749, 58, 1994, 4, 9, 40, 90, 400, 900, 3999, 1]
    for n in examples:
        print(n, "->", int_to_roman_lookup(n))

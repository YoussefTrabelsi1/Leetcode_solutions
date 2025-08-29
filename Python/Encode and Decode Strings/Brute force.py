# Brute force: escape + delimiter
# - Delimiter: '|'
# - Escape char: '\'
# - We escape '\' as '\\' and '|' as '\|', then join by '|'

from typing import List

class CodecEscape:
    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            s = s.replace("\\", "\\\\").replace("|", "\\|")
            parts.append(s)
        return "|".join(parts)

    def decode(self, s: str) -> List[str]:
        res, cur, i, n = [], [], 0, len(s)
        while i < n:
            ch = s[i]
            if ch == "\\":  # next char is literal
                if i + 1 < n:
                    cur.append(s[i + 1])
                    i += 2
                else:
                    # dangling backslash at end -> treat as literal
                    cur.append("\\")
                    i += 1
            elif ch == "|":
                res.append("".join(cur))
                cur = []
                i += 1
            else:
                cur.append(ch)
                i += 1
        # last segment (even for empty input it yields [] correctly)
        if cur or (n > 0 and s[-1] == "|"):
            res.append("".join(cur))
        return res

if __name__ == "__main__":
    codec = CodecEscape()
    for arr in [
        ["neet", "code", "love", "you"],
        ["we", "say", ":", "yes"],
        ["|", "\\", "a|b\\c", ""],
        []
    ]:
        enc = codec.encode(arr)
        dec = codec.decode(enc)
        print(arr, "->", enc, "->", dec)
        assert dec == arr
    print("CodecEscape OK")

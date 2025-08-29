# Length-prefixed decimal with '#'
# Example: ["ab", "c"] -> "2#ab1#c"
# Works with any UTF-8 content because we prefix the exact character count.

from typing import List

class CodecLenHash:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res, i, n = [], 0, len(s)
        while i < n:
            # find the delimiter '#'
            j = i
            while j < n and s[j] != "#":
                j += 1
            if j == n:
                # malformed (no '#'); tolerate as empty remainder
                break
            length = int(s[i:j])  # may be 0
            j += 1  # skip '#'
            res.append(s[j:j + length])
            i = j + length
        return res

if __name__ == "__main__":
    codec = CodecLenHash()
    for arr in [
        ["neet", "code", "love", "you"],
        ["we", "say", ":", "yes"],
        ["#", "123#456", "", "你好", "🙂"],
        []
    ]:
        enc = codec.encode(arr)
        dec = codec.decode(enc)
        print(arr, "->", enc, "->", dec)
        assert dec == arr
    print("CodecLenHash OK")

# Fixed 4-byte header + UTF-8 payload, transported via latin1 as a single string.
# This is typically the most efficient approach.

from typing import List
import struct

class CodecBinary:
    def encode(self, strs: List[str]) -> str:
        out = bytearray()
        for s in strs:
            b = s.encode("utf-8")
            out += struct.pack(">I", len(b))  # 4 bytes, big-endian
            out += b
        # Use latin1 to map bytes 0..255 to the same code points (round-trippable)
        return out.decode("latin1")

    def decode(self, s: str) -> List[str]:
        b = s.encode("latin1")
        res, i, n = [], 0, len(b)
        while i < n:
            if i + 4 > n:
                # Malformed trailing bytes; stop or raise
                break
            (L,) = struct.unpack(">I", b[i:i+4])
            i += 4
            chunk = b[i:i+L]
            i += L
            res.append(chunk.decode("utf-8"))
        return res

if __name__ == "__main__":
    codec = CodecBinary()
    for arr in [
        ["neet", "code", "love", "you"],
        ["we", "say", ":", "yes"],
        ["", "éèà", "🙂🚀", "长字符串" * 10, "has#digits123#"],
        []
    ]:
        enc = codec.encode(arr)
        dec = codec.decode(enc)
        # Note: enc may contain non-printable characters; that's fine.
        print(arr, "->", f"[encoded length: {len(enc)} chars]", "->", dec)
        assert dec == arr
    print("CodecBinary OK")

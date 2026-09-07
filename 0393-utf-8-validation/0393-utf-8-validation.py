class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        remaining = 0  # continuation bytes expected

        for byte in data:
            byte &= 0xFF  # only lowest 8 bits matter

            if remaining == 0:
                # Determine number of bytes in this character from leading bits
                if byte >> 7 == 0b0:
                    remaining = 0                     # 1-byte char: 0xxxxxxx
                elif byte >> 5 == 0b110:
                    remaining = 1                     # 2-byte char: 110xxxxx
                elif byte >> 4 == 0b1110:
                    remaining = 2                     # 3-byte char: 1110xxxx
                elif byte >> 3 == 0b11110:
                    remaining = 3                     # 4-byte char: 11110xxx
                else:
                    return False                      # invalid leading byte
            else:
                # Must be a continuation byte: 10xxxxxx
                if byte >> 6 != 0b10:
                    return False
                remaining -= 1

        return remaining == 0
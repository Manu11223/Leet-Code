class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = False
        seen_dot = False
        seen_exp = False

        for i, ch in enumerate(s):
            if ch.isdigit():
                seen_digit = True
            elif ch in ('+', '-'):
                # sign must be first char overall, or immediately after 'e'/'E'
                if i > 0 and s[i - 1] not in ('e', 'E'):
                    return False
            elif ch == '.':
                # only one dot allowed, and not after exponent
                if seen_dot or seen_exp:
                    return False
                seen_dot = True
            elif ch in ('e', 'E'):
                # only one exponent allowed, and must have seen a digit before it
                if seen_exp or not seen_digit:
                    return False
                seen_exp = True
                seen_digit = False  # require at least one digit after 'e'
            else:
                return False  # any other character is invalid

        return seen_digit
class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"

        for _ in range(n - 1):
            result = []
            i = 0
            length = len(s)

            while i < length:
                ch = s[i]
                j = i
                while j < length and s[j] == ch:
                    j += 1
                result.append(str(j - i))
                result.append(ch)
                i = j

            s = "".join(result)

        return s
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        # Use the shortest string as the candidate prefix bound
        first = min(strs, key=len)

        for i, char in enumerate(first):
            for s in strs:
                if s[i] != char:
                    return first[:i]

        return first
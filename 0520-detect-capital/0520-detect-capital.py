class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upper = sum(c.isupper() for c in word)
        return upper == 0 or upper == len(word) or (upper == 1 and word[0].isupper())
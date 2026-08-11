class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()          # splits on any whitespace, ignores extras/leading/trailing
        return ' '.join(reversed(words))
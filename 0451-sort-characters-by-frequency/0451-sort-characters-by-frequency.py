class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1

        n = len(s)
        # buckets[i] = list of chars with frequency i
        buckets = [[] for _ in range(n + 1)]
        for char, freq in count.items():
            buckets[freq].append(char)

        result = []
        for freq in range(n, 0, -1):
            for char in buckets[freq]:
                result.append(char * freq)

        return ''.join(result)
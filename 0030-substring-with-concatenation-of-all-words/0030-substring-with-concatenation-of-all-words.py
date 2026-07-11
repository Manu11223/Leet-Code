from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_freq = Counter(words)

        res = []

        for i in range(word_len):
            left = i
            count = 0
            curr = {}

            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]

                if word in word_freq:
                    curr[word] = curr.get(word, 0) + 1
                    count += 1

                    while curr[word] > word_freq[word]:
                        left_word = s[left:left + word_len]
                        curr[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == word_count:
                        res.append(left)
                        left_word = s[left:left + word_len]
                        curr[left_word] -= 1
                        left += word_len
                        count -= 1
                else:
                    curr.clear()
                    count = 0
                    left = j + word_len

        return res
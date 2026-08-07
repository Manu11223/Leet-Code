class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memo = {}
        
        def backtrack(start):
            if start in memo:
                return memo[start]
            
            if start == len(s):
                return [""]  # base case: empty suffix has one valid "sentence" - the empty one
            
            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    rest_sentences = backtrack(end)
                    for rest in rest_sentences:
                        # combine current word with the rest, handling spacing
                        sentence = word if not rest else word + " " + rest
                        sentences.append(sentence)
            
            memo[start] = sentences
            return sentences
        
        return backtrack(0)
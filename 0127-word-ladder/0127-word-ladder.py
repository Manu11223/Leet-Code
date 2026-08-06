class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        wordSet.discard(beginWord)
        
        front = {beginWord}
        back = {endWord}
        length = 1
        
        while front and back:
            # always expand the smaller frontier for efficiency
            if len(front) > len(back):
                front, back = back, front
            
            next_front = set()
            for word in front:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == word[i]:
                            continue
                        new_word = word[:i] + c + word[i+1:]
                        
                        if new_word in back:
                            return length + 1  # frontiers met
                        
                        if new_word in wordSet:
                            wordSet.discard(new_word)
                            next_front.add(new_word)
            
            front = next_front
            length += 1
        
        return 0
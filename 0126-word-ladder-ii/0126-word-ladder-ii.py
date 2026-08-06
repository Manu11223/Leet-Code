from collections import defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        L = len(beginWord)
        
        # Precompute pattern -> list of words sharing that pattern (built once, O(N*L))
        pattern_dict = defaultdict(list)
        allWords = wordSet | {beginWord}
        for word in allWords:
            for i in range(L):
                pattern = word[:i] + '*' + word[i+1:]
                pattern_dict[pattern].append(word)
        
        wordSet.discard(beginWord)
        layer = {beginWord}
        visited = {beginWord}
        children = defaultdict(list)
        found = False
        
        while layer and not found:
            next_layer = defaultdict(set)  # new_word -> set of words in current layer leading to it
            
            for word in layer:
                for i in range(L):
                    pattern = word[:i] + '*' + word[i+1:]
                    for new_word in pattern_dict.get(pattern, []):
                        if new_word == word:
                            continue
                        if new_word in wordSet and new_word not in visited:
                            next_layer[new_word].add(word)
            
            # mark this level's words visited so we never revisit / reuse them
            for w in next_layer:
                visited.add(w)
            wordSet -= set(next_layer.keys())
            
            for new_word, prevs in next_layer.items():
                children[new_word] = list(prevs)  # store predecessors here instead
            
            if endWord in next_layer:
                found = True
            
            layer = set(next_layer.keys())
        
        if not found:
            return []
        
        # Reconstruct paths by walking BACKWARD from endWord using predecessor map,
        # which avoids the forward children-explosion issue on dense graphs.
        result = []
        path = [endWord]
        
        def backtrack(word):
            if word == beginWord:
                result.append(path[::-1])
                return
            for prev in children[word]:
                path.append(prev)
                backtrack(prev)
                path.pop()
        
        backtrack(endWord)
        return result
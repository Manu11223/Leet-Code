class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        # sort by height desc, then by k asc
        people.sort(key=lambda p: (-p[0], p[1]))
        
        result = []
        for person in people:
            result.insert(person[1], person)
        
        return result
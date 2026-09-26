import math

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        rounds = minutesToTest // minutesToDie + 1
        if rounds == 1:
            # Can't test at all in time; each pig can only distinguish 1 bucket,
            # so we'd need `buckets` pigs (bucket>=1 guaranteed by constraints).
            return buckets - 1 if buckets > 0 else 0
        
        pigs = 0
        combinations = 1
        while combinations < buckets:
            combinations *= rounds
            pigs += 1
        
        return pigs
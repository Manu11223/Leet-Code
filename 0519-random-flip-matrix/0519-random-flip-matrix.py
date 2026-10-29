import random

class Solution:
    def __init__(self, m: int, n: int):
        self.n = n
        self.size = m * n      # total number of cells
        self.remaining = self.size  # unflipped cells = active range [0, remaining)
        self.swapped = {}      # virtual array: position -> value (default: itself)

    def flip(self) -> list[int]:
        r = random.randrange(self.remaining)  # exactly 1 random call
        self.remaining -= 1

        # value currently living at position r
        idx = self.swapped.get(r, r)
        # move the value at the last active position into slot r
        self.swapped[r] = self.swapped.get(self.remaining, self.remaining)

        return [idx // self.n, idx % self.n]

    def reset(self) -> None:
        self.remaining = self.size
        self.swapped.clear()
        



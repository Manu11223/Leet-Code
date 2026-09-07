class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1
        step = 1
        remaining = n
        left = True

        while remaining > 1:
            # Head changes when eliminating from left
            # OR when eliminating from right with odd count
            if left or remaining % 2 == 1:
                head += step

            remaining //= 2
            step *= 2
            left = not left

        return head
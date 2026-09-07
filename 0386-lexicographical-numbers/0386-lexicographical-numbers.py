class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        curr = 1
        for _ in range(n):
            result.append(curr)
            if curr * 10 <= n:
                # Step into first child: curr -> curr0
                curr *= 10
            else:
                # Move to next sibling, backtracking as needed
                while curr % 10 == 9 or curr + 1 > n:
                    curr //= 10
                curr += 1
        return result
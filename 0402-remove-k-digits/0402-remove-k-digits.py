class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # if k still > 0, remove from the end (already increasing, so trailing digits are largest)
        if k > 0:
            stack = stack[:-k]
        
        # strip leading zeros
        result = ''.join(stack).lstrip('0')
        
        return result if result else "0"
class Solution:
    def findNthDigit(self, n: int) -> int:
        digit_length = 1
        count = 9          # how many numbers have `digit_length` digits
        start = 1           # first number with `digit_length` digits
        
        while n > digit_length * count:
            n -= digit_length * count
            digit_length += 1
            count *= 10
            start *= 10
        
        # the target number is the (n-1)//digit_length-th number after `start`
        number = start + (n - 1) // digit_length
        digit_index = (n - 1) % digit_length
        
        return int(str(number)[digit_index])
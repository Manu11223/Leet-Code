class Solution:
    def compress(self, chars: list[str]) -> int:
        write = 0
        read = 0
        n = len(chars)

        while read < n:
            char = chars[read]
            group_start = read
            while read < n and chars[read] == char:
                read += 1
            group_len = read - group_start

            chars[write] = char
            write += 1

            if group_len > 1:
                for digit in str(group_len):
                    chars[write] = digit
                    write += 1

        return write
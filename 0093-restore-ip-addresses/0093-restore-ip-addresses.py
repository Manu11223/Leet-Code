class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        n = len(s)
        result = []
        segments = []

        def is_valid(segment: str) -> bool:
            if len(segment) > 1 and segment[0] == '0':
                return False
            return 0 <= int(segment) <= 255

        def backtrack(start: int) -> None:
            if len(segments) == 4:
                if start == n:
                    result.append('.'.join(segments))
                return

            remaining_segments = 4 - len(segments)
            remaining_chars = n - start
            if remaining_chars < remaining_segments or remaining_chars > remaining_segments * 3:
                return

            for length in range(1, 4):
                if start + length > n:
                    break
                segment = s[start:start + length]
                if is_valid(segment):
                    segments.append(segment)
                    backtrack(start + length)
                    segments.pop()

        backtrack(0)
        return result
        
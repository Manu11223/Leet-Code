class Solution:
    def lengthLongestPath(self, input: str) -> int:
        path_len = [0] * (input.count('\n') + 2)  # path_len[depth] = cumulative length up to this depth
        max_len = 0

        for line in input.split('\n'):
            # depth = number of leading tabs
            name = line.lstrip('\t')
            depth = len(line) - len(name)

            if '.' in name:
                # It's a file: compute full path length
                # path_len[depth] is parent's cumulative length (0 if depth==0)
                current_len = path_len[depth] + len(name)
                max_len = max(max_len, current_len)
            else:
                # It's a directory: store cumulative length including a '/' separator
                path_len[depth + 1] = path_len[depth] + len(name) + 1

        return max_len
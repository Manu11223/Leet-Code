class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empties = []

        def box_index(r, c):
            return (r // 3) * 3 + (c // 3)

        for r in range(9):
            for c in range(9):
                ch = board[r][c]
                if ch == '.':
                    empties.append((r, c))
                else:
                    bit = 1 << (int(ch) - 1)
                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[box_index(r, c)] |= bit

        n = len(empties)

        def backtrack(idx):
            if idx == n:
                return True

            r, c = empties[idx]
            b = box_index(r, c)
            used = rows[r] | cols[c] | boxes[b]
            available = (~used) & 0x1FF  # 9 bits for digits 1-9

            while available:
                bit = available & (-available)  # lowest set bit
                available ^= bit
                digit = bit.bit_length()  # 1-9

                # place
                rows[r] |= bit
                cols[c] |= bit
                boxes[b] |= bit
                board[r][c] = str(digit)

                if backtrack(idx + 1):
                    return True

                # undo
                rows[r] ^= bit
                cols[c] ^= bit
                boxes[b] ^= bit
                board[r][c] = '.'

            return False

        backtrack(0)
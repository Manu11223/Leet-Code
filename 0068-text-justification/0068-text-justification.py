class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result = []
        line = []
        line_len = 0

        for word in words:
            # check if adding this word (plus separating spaces) fits
            if line_len + len(line) + len(word) > maxWidth:
                result.append(self._justify_line(line, line_len, maxWidth))
                line = []
                line_len = 0

            line.append(word)
            line_len += len(word)

        # last line: left-justified
        last_line = ' '.join(line)
        last_line += ' ' * (maxWidth - len(last_line))
        result.append(last_line)

        return result

    def _justify_line(self, line: list[str], line_len: int, maxWidth: int) -> str:
        if len(line) == 1:
            return line[0] + ' ' * (maxWidth - line_len)

        total_spaces = maxWidth - line_len
        gaps = len(line) - 1
        base_space, extra = divmod(total_spaces, gaps)

        parts = []
        for i, word in enumerate(line[:-1]):
            parts.append(word)
            # leftmost gaps get one extra space when it doesn't divide evenly
            spaces = base_space + (1 if i < extra else 0)
            parts.append(' ' * spaces)
        parts.append(line[-1])

        return ''.join(parts)
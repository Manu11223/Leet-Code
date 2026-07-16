class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        i = j = 0
        star_idx = -1   # position in p of last '*' seen
        s_backup = -1   # position in s to retry from after that '*'

        while i < m:
            if j < n and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1
            elif j < n and p[j] == '*':
                star_idx = j
                s_backup = i
                j += 1  # tentatively match empty sequence
            elif star_idx != -1:
                # backtrack: let '*' consume one more char of s
                j = star_idx + 1
                s_backup += 1
                i = s_backup
            else:
                return False

        # consume any trailing '*' characters in p
        while j < n and p[j] == '*':
            j += 1

        return j == n
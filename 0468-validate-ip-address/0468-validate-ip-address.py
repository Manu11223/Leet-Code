class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP:
            parts = queryIP.split('.')
            if len(parts) != 4:
                return "Neither"
            for p in parts:
                if not p or len(p) > 3 or not p.isdigit():
                    return "Neither"
                if len(p) > 1 and p[0] == '0':
                    return "Neither"
                if int(p) > 255:
                    return "Neither"
            return "IPv4"

        if ':' in queryIP:
            parts = queryIP.split(':')
            if len(parts) != 8:
                return "Neither"
            hex_chars = set("0123456789abcdefABCDEF")
            for p in parts:
                if not 1 <= len(p) <= 4:
                    return "Neither"
                if any(c not in hex_chars for c in p):
                    return "Neither"
            return "IPv6"

        return "Neither"
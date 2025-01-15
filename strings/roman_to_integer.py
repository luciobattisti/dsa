# https://leetcode.com/problems/roman-to-integer

class Solution:
    def romanToInt(self, s: str) -> int:

        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        # Base case
        if len(s) == 1:
            return symbols[s[0]]

        # General case
        total = 0
        p1 = 0
        while p1 < len(s):
            if p1+1 < len(s):
                next_char = s[p1+1]
            else:
                next_char = ""

            combo = s[p1] + next_char
            if combo in symbols:
                total += symbols[combo]
                p1 += 2
            else:
                total += symbols[s[p1]]
                p1 += 1

        return total


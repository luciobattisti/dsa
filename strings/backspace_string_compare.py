# https://leetcode.com/problems/backspace-string-compare/
# Similar problems:
# https://leetcode.com/problems/crawler-log-folder/


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def check_value(a, p):
            if p >= 0:
                return a[p]
            else:
                return ""

        print(s, t)

        # Edge cases
        if len(s) == 1 and len(t) == 1:  # O(1)
            return s == t

        p1 = len(s) - 1
        p2 = len(t) - 1

        count = 0
        while p1 >= 0 or p2 >= 0:

            print(p1, p2, check_value(s, p1), check_value(t, p2))

            if check_value(s, p1) == "#" or check_value(t, p2) == "#":
                if check_value(s, p1) == "#":
                    move_left = 2
                    while move_left > 0:
                        p1 -= 1
                        move_left -= 1
                        if check_value(s, p1) == "#":
                            move_left += 2

                if check_value(t, p2) == "#":
                    move_left = 2
                    while move_left > 0:
                        p2 -= 1
                        move_left -= 1
                        if check_value(t, p2) == "#":
                            move_left += 2
            else:
                if check_value(s, p1) != check_value(t, p2):
                    return False
                else:
                    p1 -= 1
                    p2 -= 1

        return True

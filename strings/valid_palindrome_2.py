# https://leetcode.com/problems/valid-palindrome-ii/
# Similar questions:
#


def is_palindrome(s: str, p1: int, p2: int) -> bool:
    while p2 > p1:
        if s[p1] == s[p2]:
            p1 += 1
            p2 -= 1
        else:
            return False

    return True


class Solution:
    def validPalindrome(self, s: str) -> bool:

        # Edge cases
        if len(s) <= 2:
            return True

        # General case
        p1 = 0
        p2 = len(s) - 1
        num_deletions = 0

        while p2 > p1:
            if s[p1] == s[p2]:
                p1 += 1
                p2 -= 1
            else:
                # Try to remove left character
                palindrome_check = is_palindrome(s, p1 + 1, p2)

                if palindrome_check:
                    return True
                else:
                    # Try to remove right character
                    return is_palindrome(s, p1, p2 - 1)

        return True

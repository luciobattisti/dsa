# https://leetcode.com/problems/valid-palindrome
# Similar problems:
# https://leetcode.com/problems/palindrome-linked-list/
# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/



class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Edge case
        if len(s) <= 1:
            return True

        # General case
        p1 = 0
        p2 = len(s) - 1

        while p2 > p1:

            if not s[p1].isalnum():
                p1 += 1

            if not s[p2].isalnum():
                p2 -= 1

            if s[p1].lower().isalnum() and s[p2].lower().isalnum():
                if s[p1].lower() != s[p2].lower():
                    return False
                else:
                    p1 += 1
                    p2 -= 1

        return True

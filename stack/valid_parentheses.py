# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 1:
            return False

        pars = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        stack = []
        for curr_p in s:
            if curr_p in pars:
                stack.append(curr_p)
            else:
                if not stack:
                    return False
                if pars[stack.pop()] != curr_p:
                    return False

        if not stack:
            return True
        else:
            return False

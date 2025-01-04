# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        # Edge cases
        if not s:
            return True

        stack = []
        output = []

        pars = {"(", ")"}

        offset = 0
        for i in range(0, len(s)):
            curr_c = s[i]
            if curr_c not in pars:
                output.append(curr_c)
            else:
                if curr_c == "(":
                    stack.append(i)
                    output.append(curr_c)
                else:
                    if not stack:
                        offset += 1
                    else:
                        stack.pop()
                        output.append(curr_c)

        while stack:
            index_to_remove = stack.pop() - offset
            output.pop(index_to_remove)

        return "".join(output)

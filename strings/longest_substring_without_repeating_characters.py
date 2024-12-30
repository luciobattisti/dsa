# https://leetcode.com/problems/longest-substring-without-repeating-characters
# Similar problem:
# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) <= 1:
            return len(s)

        p1 = 0
        p2 = 0
        max_len = 0
        cur_sub = set()

        while p1 < len(s) and p2 < len(s):

            if s[p2] not in cur_sub:
                cur_sub.add(s[p2])
                max_len = max(max_len, len(cur_sub))
                p2 += 1
            else:
                while s[p2] in cur_sub:
                    cur_sub.remove(s[p1])
                    p1 += 1

        return max_len

# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Similar problems:
# https://leetcode.com/problems/first-bad-version/description/
# https://leetcode.com/problems/plates-between-candles/description/
# https://leetcode.com/problems/find-target-indices-after-sorting-array/description/
def recurse(a, l, r, t):
    length = r - l + 1

    # Base case
    if length <= 1:
        if a[l] == t:
            li = find_left_index(a, l, t)
            ri = find_right_index(a, l, t)

            return [li, ri]
        else:
            return [-1, -1]

    # Recursive case
    m = (l + r) // 2
    if t == a[m]:
        li = find_left_index(a, m, t)
        ri = find_right_index(a, m, t)

        return [li, ri]
    elif t < a[m]:
        # Recurse left
        return recurse(a, l, m - 1, t)
    else:
        # Recurse right
        return recurse(a, m + 1, r, t)


def find_left_index(a, m, t):
    if m == 0:
        return m

    while m > 0:
        if a[m - 1] == t:
            m -= 1
        else:
            break

    return m


def find_right_index(a, m, t):
    print(m)
    if m == len(a) - 1:
        return m

    while m < len(a) - 1:
        if a[m + 1] == t:
            m += 1
        else:
            break

    return m


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # Edge cases
        if len(nums) == 0:
            return [-1, -1]

        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        # Standard case
        l = 0
        r = len(nums) - 1
        return recurse(nums, l, r, target)

# https://leetcode.com/problems/partition-array-according-to-given-pivot/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        count = 0

        left = []
        right = []

        for p1 in range(len(nums)):
            if nums[p1] < pivot:
                left.append(nums[p1])
            elif nums[p1] > pivot:
                right.append(nums[p1])
            else:
                count += 1

        res = left + ([pivot] * count) + right

        return res


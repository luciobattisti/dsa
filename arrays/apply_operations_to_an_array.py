# https://leetcode.com/problems/apply-operations-to-an-array/description

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        zero = []
        non_zero = []
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            if nums[i] == 0:
                zero.append(nums[i])
            else:
                non_zero.append(nums[i])

        if nums[len(nums) - 1] == 0:
            zero.append(nums[len(nums) - 1])
        else:
            non_zero.append(nums[len(nums) - 1])

        return non_zero + zero

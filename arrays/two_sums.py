# https://leetcode.com/problems/two-sum
# Similar problems:
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

from typing import List, Optional


class Solution:

    def twoSum(self, nums: List[int], target: int) -> Optional[List[int]]:

        if not nums or len(nums) == 1:
            return None
        elif len(nums) == 2:
            if (nums[0] + nums[1]) == target:
                return [0,1]

        nums_dict = {}

        for p1 in range(0, len(nums)):
            num_to_find = target - nums[p1] # num_to_find = 7

            if num_to_find in nums_dict:
                return [p1, nums_dict[num_to_find]]
            else:
                nums_dict[nums[p1]] = p1

        return None

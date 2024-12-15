import random
# https://leetcode.com/problems/kth-largest-element-in-an-array/


def partition(nums: List[int], l: int, r: int, p: int) -> int:
    # Swap pivot with righmost element
    nums[p], nums[r] = nums[r], nums[p]

    # Initialize store index to leftmost index
    s = l

    # Traverse array until l reaches r
    # Compare left item with pivot
    # All elements that are less than pivot should stay on the left
    while l < r:
        if nums[l] < nums[r]:
            nums[l], nums[s] = nums[s], nums[l]
            s += 1

        l += 1

    # Swap back pivot with s
    nums[s], nums[r] = nums[r], nums[s]

    return s


def quick_select(nums: List[int], l: int, r: int, k: int):
    # Pick random element as pivot
    p = random.randint(l, r)

    # Partition
    s = partition(nums, l, r, p)

    if s == k:
        return nums[s]
    elif s < k:
        return quick_select(nums, s + 1, r, k)
    else:
        return quick_select(nums, l, s - 1, k)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Edge case
        if len(nums) == 1:
            return nums[0]

        # Define k for largest element
        k = len(nums) - k

        largest_kth = quick_select(nums, 0, len(nums) - 1, k)

        return largest_kth


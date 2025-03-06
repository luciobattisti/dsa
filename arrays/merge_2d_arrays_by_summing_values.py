# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:

        p1 = 0
        p2 = 0

        result = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1][0] == nums2[p2][0]:
                result.append([nums1[p1][0], nums1[p1][1] + nums2[p2][1]])
                p1 += 1
                p2 += 1
            elif nums1[p1][0] < nums2[p2][0]:
                result.append(nums1[p1])
                p1 += 1
            else:
                result.append(nums2[p2])
                p2 += 1

        while p1 < len(nums1):
            result.append(nums1[p1])
            p1 += 1

        while p2 < len(nums2):
            result.append(nums2[p2])
            p2 += 1

        return result

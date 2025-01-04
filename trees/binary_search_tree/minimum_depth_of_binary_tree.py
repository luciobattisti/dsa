# https://leetcode.com/problems/minimum-depth-of-binary-tree/

import heapq
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


def min_depth_helper(node: TreeNode, depth: int, min_depth: list):
    # Base case
    if not node.left and not node.right:
        heapq.heappush(min_depth, depth)

    # Recursive case
    if node.left:
        min_depth_helper(node.left, depth + 1, min_depth)

    if node.right:
        min_depth_helper(node.right, depth + 1, min_depth)


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Edge case
        if not root:
            return 0

        depth = 1
        min_depth = []

        min_depth_helper(root, depth, min_depth)

        return heapq.heappop(min_depth)


def find_min_depth_no_heapq(node: TreeNode, depth: int, min_depth: list) -> None:
    # Base case: Leaf node
    if not node.left and not node.right:
        min_depth[0] = min(min_depth[0], depth)

    # Recursive case: Traverse left and right subtrees
    if node.left:
        find_min_depth_no_heapq(node.left, depth + 1, min_depth)

    if node.right:
        find_min_depth_no_heapq(node.right, depth + 1, min_depth)


class SolutionNoHeapq:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Edge case: Empty tree
        if not root:
            return 0

        # Initialize minimum depth to a large value
        min_depth = [int('inf')]

        # Start traversal
        find_min_depth_no_heapq(root, 1, min_depth)

        return min_depth[0]

# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Similar problems:
# https://leetcode.com/problems/balanced-binary-tree/description/
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth_helper(node: TreeNode, depth: int) -> int:
    # Anytime we visit a node, we increase the depth
    depth += 1

    # Base case
    # Node has no children
    if not node.left and not node.right:
        return depth

    # Recursive cases
    # Node has at least one child
    if node.left and not node.right:
        return max_depth_helper(node.left, depth)

    if node.right and not node.left:
        return max_depth_helper(node.right, depth)

    if node.right and node.left:
        return max(
            max_depth_helper(node.left, depth),
            max_depth_helper(node.right, depth)
        )


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = max_depth_helper(root, 0)

        return depth


# Simplified solution

class SimplifiedSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)

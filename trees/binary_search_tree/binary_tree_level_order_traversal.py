# https://leetcode.com/problems/binary-tree-level-order-traversal

from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def level_order_traversal(node: TreeNode, d: int, level_order: dict):
    if d not in level_order:
        level_order[d] = [node.val]
    else:
        level_order[d].append(node.val)

    if node.left:
        level_order_traversal(node.left, d + 1, level_order)

    if node.right:
        level_order_traversal(node.right, d + 1, level_order)


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # Edge case
        if not root:
            return []

        level_order = {}
        d = 0
        level_order_traversal(root, d, level_order)

        level_order_output = []
        for i in range(len(level_order.keys())):
            level_order_output.append(level_order[i])

        return level_order_output


class BFSSolution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # Edge case
        if not root:
            return []

        level_order = []
        queue = deque()

        queue.append(root)

        level_order_traversal = []
        while queue:
            level_order = []

            for _ in range(len(queue)):
                node = queue.popleft()
                level_order.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            level_order_traversal.append(level_order)

        return level_order_traversal






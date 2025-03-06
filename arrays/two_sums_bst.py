# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_target(node: TreeNode, target: int) -> TreeNode:
    if not node:
        return None

    if node.val == target:
        return node

    if target < node.val:
        return find_target(node.left, target)
    else:
        return find_target(node.right, target)


def traversal(node: TreeNode, target: int, root: TreeNode) -> bool:
    desired_num = target - node.val

    target_node = find_target(root, desired_num)
    if target_node:
        if target_node != node:
            return True

    left_result = False
    if node.left:
        left_result = traversal(node.left, target, root)

    right_result = False
    if node.right:
        right_result = traversal(node.right, target, root)

    return left_result or right_result


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # Start at the root of the tree
        # In Example 1, we have 5 so desired_num = 9-5 = 4
        # Seach for 4. Perform a depth first search
        # If 4 is found return True

        if not root.left and not root.right:
            return False

        return traversal(root, k, root)

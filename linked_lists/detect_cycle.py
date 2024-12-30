# https://leetcode.com/problems/linked-list-cycle-ii/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr_node = head
        nodes = set()

        while curr_node:
            nodes.add(curr_node)

            if curr_node.next in nodes:
                return curr_node.next
            else:
                curr_node = curr_node.next

        return None

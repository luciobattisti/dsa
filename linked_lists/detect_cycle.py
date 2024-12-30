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


class SolutionFloydsTortoiseHare:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return None
        elif head.next == head:
            return head

        # Detect cycle
        slow = head
        fast = head
        meeting_node = None

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                meeting_node = slow
                break

        if not meeting_node:
            return None

        # Detect start of cycle
        slow = meeting_node
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

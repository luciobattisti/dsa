# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse(head: ListNode, tail: ListNode) -> ListNode:
    curr_node = head
    prev_node = None

    while curr_node != tail:
        next_node = curr_node.next
        curr_node.next = prev_node

        prev_node = curr_node
        curr_node = next_node

    curr_node.next = prev_node

    return curr_node


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        # Edge cases
        if left == right:
            return head

        # General case

        # Find left node and right node
        prev_node = None
        curr_node = head
        counter = 1
        while counter < right:

            if counter == left:
                left_node = curr_node
                left_node_prev = prev_node

            prev_node = curr_node
            counter += 1
            curr_node = curr_node.next

        right_node = curr_node
        right_node_next = curr_node.next

        # if left_node_prev:
        #    print(f"Left node prev: {left_node_prev.val}")

        # print(f"Left node: {left_node.val}")

        # if right_node_next:
        #    print(f"Right node next: {right_node_next.val}")

        # print(f"Right node {right_node.val}")

        # Reverse sub list
        reversed_head = reverse(left_node, right_node)

        if left_node_prev:
            left_node_prev.next = reversed_head
        else:
            head = reversed_head

        if right_node_next:
            left_node.next = right_node_next

        return head

class ListNode:

    def __init__(self, value: any, next_node):
        self.value = value
        self.next = next_node


class LinkedList:

    def __init__(self, head: ListNode):
        self.head = head

    def add_items(self, items: list):
        curr_node = self.head
        for _item in items:
            curr_node.next = ListNode(_item, None)
            curr_node = curr_node.next

    def print_items(self):
        print("Items:")

        curr_node = self.head
        while curr_node:
            print(curr_node.value)
            curr_node = curr_node.next

    def reverse(self):

        prev_node = None
        curr_node = self.head

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        self.head = prev_node


if __name__ == "__main__":
    # Init Linked List
    head = ListNode(1, None)
    linked_list = LinkedList(head)

    # Add items to Linked List
    linked_list.add_items([2, 3, 4, 5])

    # Print values
    linked_list.print_items()

    # Reverse linked list
    linked_list.reverse()
    print("Reversal:")
    linked_list.print_items()
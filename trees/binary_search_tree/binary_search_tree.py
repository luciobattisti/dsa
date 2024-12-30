from typing import Any, Optional, Union, Tuple


class Node:
    """A Node in the Binary Search Tree."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.key})"


class BinarySearchTree:
    """Binary Search Tree implementation."""
    def __init__(self):
        self.root = None

    def _insert_helper(self, node, key):

        if key >= node.key:
            if not node.right:
                node.right = Node(key)
            else:
                self._insert_helper(node.right, key)
        else:
            if not node.left:
                node.left = Node(key)
            else:
                self._insert_helper(node.left, key)

    def insert(self, key):
        """
        Insert a key into the BST.
        To be implemented.
        """

        if not self.root:
            self.root = Node(key)
        else:
            self._insert_helper(self.root, key)

    def _search_helper(self, node:Node, key: Any) -> Optional[Node]:

        if key == node.key:
            return node
        elif key > node.key:
            if node.right:
                return self._search_helper(node.right, key)
            else:
                return None
        else:
            if node.left:
                return self._search_helper(node.left, key)
            else:
                return None

    def search(self, key) -> Any:
        """
        Search for a key in the BST.
        To be implemented.
        """

        if self.root:
            return self._search_helper(self.root, key)

    def _find_and_remove_in_order_successor(self, node: Node) -> Node:
        if node.left:
            successor_node = self._find_and_remove_in_order_successor(node.left)
            if node.left == successor_node:
                node.left = None
            return successor_node
        else:
            return node

    def _delete_helper(self, parent_node:Optional[Node], node: Node, key: Any) -> Tuple[Optional[Node], Optional[Node]]:

        if key == node.key:
            return parent_node, node
        elif key > node.key:
            if node.right:
                return self._delete_helper(node, node.right, key)
            else:
                return None, None
        else:
            if node.left:
                return self._delete_helper(node, node.left, key)
            else:
                return None, None

    def _delete_no_children(self, parent_node:Node, node:Node) -> Node:
        if not parent_node:
            self.root = None

        if node == parent_node.left:
            parent_node.left = None
        else:
            parent_node.right = None

        return node

    def _delete_one_child(self, parent_node:Node, node:Node) -> Node:
        if not parent_node:
            if node.left:
                self.root = node.left
                node.left = None
            else:
                self.root = node.right
                node.right = None

        if node.left:
            parent_node.left = node.left
            node.left = None
        else:
            parent_node.right = node.right
            node.right = None

        return node

    def _delete_two_children(self, node: Node) -> Node:
        successor_node = self._find_and_remove_in_order_successor(node.right)

        if successor_node == node.right:
            node.right = None

        node.key = successor_node.key

        return node

    def delete(self, key: Any) -> Optional[Node]:
            """
            Delete a key from the BST.
            """

            if self.root:
                parent_node, node = self._delete_helper(None, self.root, key)

                if not node:
                    return None

                if not node.left and not node.right:
                    # Delete no children node
                    return self._delete_no_children(parent_node, node)

                if not node.left or not node.right:
                    # Delete one child node
                    return self._delete_one_child(parent_node, node)

                if node.left and node.right:
                    # Delete two children node
                    print("Delete two children")
                    return self._delete_two_children(node)
            else:
                return None

    def _in_order_helper(self, node: Node, result: list):

        if node.left:
            self._in_order_helper(node.left, result)

        result.append(node.key)

        if node.right:
            self._in_order_helper(node.right, result)

    def in_order_traversal(self) -> list:
        """
        Perform in-order traversal of the BST.
        Travers the tree this way: left -> root -> right
        Useful when we need the elements in sorted order
        """
        result = []
        if self.root:
            self._in_order_helper(self.root, result)

        return result

    def _pre_order_helper(self, node: Node, result: list):
        result.append(node.key)

        if node.left:
            self._pre_order_helper(node.left, result)

        if node.right:
            self._pre_order_helper(node.right, result)

    def pre_order_traversal(self) -> list:
        """
        Perform pre-order traversal of the BST.
        Travers the tree this way: left -> root -> right
        Useful for tasks where you need to process the root before examining the children
        (e.g., creating a copy of the tree or serializing it)
        """

        result = []
        if self.root:
            self._pre_order_helper(self.root, result)

        return result

    def _post_order_helper(self, node: Node, result: list):

        if node.left:
            self._post_order_helper(node.left, result)

        if node.right:
            self._post_order_helper(node.right, result)

        result.append(node.key)

    def post_order_traversal(self) -> list:
        """
        Perform post-order traversal of the BST.
        Travers the tree this way: left -> root -> right
        Useful for tasks where children need to be processed before the root
        (e.g., deleting or freeing nodes in a tree)
        """

        result = []
        if self.root:
            self._post_order_helper(self.root, result)

        return result


# Example of instantiating the tree (without implemented methods)
if __name__ == "__main__":
    bst = BinarySearchTree()
    print(f"Empty tree: {bst.root}")

    nums = [10, 5, 15, 3, 7, 12, 18]

    for n in nums:
        bst.insert(n)

    print("In-order:", bst.in_order_traversal())
    print("Pre-order:", bst.pre_order_traversal())
    print("Post-order:", bst.post_order_traversal())

    print("Search for 15:", bst.search(15))
    print("Search for 20:", bst.search(20))

    print("Delete 15:", bst.delete(15))
    print("In-order after deletion:", bst.in_order_traversal())

    print("Delete 15:", bst.delete(21))
    print("In-order after deletion:", bst.in_order_traversal())

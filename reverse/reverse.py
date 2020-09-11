class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # BASE CASE
        if node is None:
            return
        # This checks for a single item in the list and sets the node as the head
        # No need to reverse
        elif node.next_node is None:
            self.head = node
            return self.head
        else:
            # Recursive case. sets the node.next.next as the 2nd node from current
            # This should make the recursion work backwards through the list, and return the values reversed..
            rev = self.reverse_list(node.next_node, prev)
            node.next_node.next_node = node # <- This is crazy. Thanks stack overflow
            node.next_node = prev
            return rev

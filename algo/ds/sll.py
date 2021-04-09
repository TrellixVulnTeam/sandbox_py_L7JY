class SLLNode:

    def __init__(self, data):
        self._data = data
        self._next = None

    def __str__(self):
        return f"<SLLNode: data={self._data}>"

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        self._data = new_data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, new_next):
        self._next = new_next


class SLL:

    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        node_list = [str(current)]
        while current is not None:
            current = current.next
            node_list.append(str(current))
        return f"SLL({self.size()}): {' -> '.join(node_list)}"

    def is_empty(self):
        """Returns True if the Linked List is empty. Otherwise, returns False."""
        return self.head is None

    def size(self):
        """Traverses the Linked List and returns an integer value representing
        the number of nodes in the Linked List.

        The time complexity is O(n) because every Node in the Linked List must
        be visited in order to calculate the size of the Linked List.
        """
        size = 0
        if self.head is None:
            return 0

        current = self.head
        while current is not None:  # While there are still Nodes left to count
            size += 1
            current = current.next

        return size

    def search(self, data):
        """Traverses the Linked List and returns True if the data searched for
        is present in one of the Nodes. Otherwise, it returns False.

        The time complexity is O(n) because in the worst case, we have to visit
        every Node in the list.
        """
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next

        return False

    def add_front(self, new_data):
        """Add a Node whose data is the new_data argument to the front of the
        Linked List."""
        temp = SLLNode(new_data)
        temp.next = self.head
        self.head = temp

    def remove(self, data):
        """Removes the first occurrence of a Node that contains the data argument
        as its self.data attribute and returns True. Otherwise, returns False.

        The time complexity is O(n) because in the worst case, we have to visit
        every Node before finding the one we want to remove.
        """
        current = self.head
        previous = None
        while current is not None:
            if current.data == data:
                if previous is None:  # remove head
                    self.head = current.next
                else:
                    previous.next = current.next
                return True
            else:
                previous = current
                current = current.next

        return False


if __name__ == '__main__':
    sll = SLL()
    sll.add_front(4)
    sll.add_front(2)
    sll.add_front(56)
    sll.add_front(3)
    print(sll)

    print(sll.remove(99))
    print(sll.remove(56))
    print(sll)
    print(sll.remove(3))
    print(sll)
    print(sll.remove(4))
    print(sll)
    print(sll.remove(2))
    print(sll)

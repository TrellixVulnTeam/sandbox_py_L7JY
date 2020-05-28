class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        """Accepts an item as a parameter and appends it to the end of the list.
        Returns nothing.

        The runtime for this method is O(1), or constant time, because appending
        to the end of a list happens in constant time.
        """
        self.items.append(item)

    def pop(self):
        """Removes and returns the last item for the list, which is also the
        top item of the Stack.

        The runtime here is constant time, because all it does is index to the
        last item of the list.
        """
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        """This method returns the last item in the list, which is also the item
        at the top of the Stack.

        This method runs in constant time because indexing into a list is done
        in constant time.
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """This method returns the length of the list that is representing the
        Stack.

        This method runs in constant time because finding the length of a list
        also in constant time.
        """
        return len(self.items)

    def is_empty(self):
        """This method returns a Boolean value describing whether or not the
        Stack is empty.

        Testing for equality happens in constant time.
        """
        return self.items == []

    def __str__(self):
        return str(self.items)


class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Takes in an item and inserts that item into the 0th index of the list
        that is representing the Queue.

        The runtime is O(n), or linear time, because inserting into the 0th
        index of a list forces all the other items in the list to move one index
        to the right.
        """
        self.items.insert(0, item)

    def dequeue(self):
        """Returns and removes the front-most item of the Queue, which is
        represented by the last item in the list.

        The runtime is O(1), or constant time, because indexing to the end of a
        list happens in constant time.
        """
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        """Returns the last item in the list. which represents the front-most
        item in the Queue.

        The runtime is constant because we're just indexing to the last item of
        the list and returning the value found there.
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """Returns the size of the Queue, which is represent by the length of
        the list.

        The runtime is O(1), or constant time, because we're only returning the length.
        """
        return len(self.items)

    def is_empty(self):
        """Returns a Boolean value expressing whether or not the list
        representing the Queue is empty.

        Runs in constant time, because it's only checking for equality.
        """
        return self.items == []

    def __str__(self):
        return str(self.items)


class Deque:

    def __init__(self):
        self.items = []

    def add_front(self, item):
        """Takes an item as a parameter and inserts it into the 0th index
        of the list that is representing the Deque.

        The runtime is linear, or O(n), because every time you insert into the
        front of a list, all the other items in the list need to shift one
        position to the right.
        """

        self.items.insert(0, item)

    def add_rear(self, item):
        """Takes in an item as a parameter and appends that item to the end of
        the list that is representing the Deque.

        The runtime is constant because appending to the end of a list happens
        in constant time.
        """

        self.items.append(item)

    def remove_front(self):
        """Removes and returns the item in the 0th index of the list, which
        represents the front of the Deque.

        The runtime is linear, or O(n), because when we remove an item from the
        0th index, all the other items have to shift one index to the left.
        """
        if self.items:
            return self.items.pop(0)
        return None

    def remove_rear(self):
        """Removes and returns the last item of the list, which represents the
        rear of the Deque.

        The runtime is constant because all we're doing is indexing to the end
        of a list.
        """
        if self.items:
            return self.items.pop()
        return None

    def peek_front(self):
        """Returns the value found at the 0th index of the list, which represents
        the front of the Deque.

        The runtime is constant because al we're doing is indexing into a list.
        """
        if self.items:
            return self.items[0]
        return None

    def peek_rear(self):
        """Returns the value found at the -1st, or last, index.

        The runtime is constant because all we're doing is indexing into a
        list."""
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """Returns the length of the list, which is representing the Deque.

        The runtime will be constant because all we're doing is finding the length
        of a list and returning that value."""
        return len(self.items)

    def is_empty(self):
        """Checks to see if the list representing our Deque is empty. Returns True
        if it is, or False if it isn't.

        The runtime is constant because all we're doing is comparing two values.
        """
        return self.items == []

    def __str__(self):
        return str(self.items)

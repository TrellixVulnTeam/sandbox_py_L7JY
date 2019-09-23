class Queue:
    def __init__(self):
        self.queue = []  # FIFO

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self, x):
        return self.queue.pop(0)  # dequeue top value

    def __str__(self):
        return str(self.queue)


class Stack:
    def __init__(self):
        self.stack = []  # LIFO

    def push(self, x):
        self.stack.append(x)

    def pop(self, x):
        return self.stack.pop(-1)  # pop rear value

    def __str__(self):
        return str(self.stack)


queue = Queue()
stack = Stack()


print("*********************************")
print(queue)

for i in range(5):
    queue.enqueue(i)
    print(queue)
for i in range(5):
    queue.dequeue(i)
    print(queue)

print("*********************************")
print(stack)

for i in range(5):
    stack.push(i)
    print(stack)
for i in range(5):
    stack.pop(i)
    print(stack)

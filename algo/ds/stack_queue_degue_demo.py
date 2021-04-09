from data_structures import Stack, Queue, Deque

stack = Stack()
queue = Queue()
deque = Deque()

print("*** Stack ***")
print(stack)

for i in range(5):
    stack.push(i)
    print(stack)
for i in range(stack.size()):
    stack.pop()
    print(stack)

print("*** Queue ***")
print(queue)

for i in range(5):
    queue.enqueue(i)
    print(queue)
for i in range(queue.size()):
    queue.dequeue()
    print(queue)

print("*** Deque - Stack operation ***")
print(deque)

for i in range(5):
    deque.add_rear(i)
    print(deque)
for i in range(deque.size()):
    deque.remove_rear()
    print(deque)

print("*** Deque - Queue operation ***")
print(deque)

for i in range(5):
    deque.add_front(i)
    print(deque)
for i in range(deque.size()):
    deque.remove_rear()
    print(deque)

from algo.ds.data_structures import Queue

import random


class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm  # pages per minute
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task is not None:
            return True
        else:
            return False

    def start_next(self, task):
        self.current_task = task
        self.time_remaining = task.get_pages() * 60 / self.page_rate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp


def simulation(seconds, ppm):
    printer = Printer(ppm)
    print_queue = Queue()
    waiting_times = []

    for sec in range(seconds):
        if is_new_task():
            task = Task(sec)
            print_queue.enqueue(task)

        if not printer.busy() and not print_queue.is_empty():
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(sec))
            printer.start_next(next_task)

        printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average Wait %6.2f secs %3d tasks remaining." % (average_wait, print_queue.size()))


def is_new_task():
    return random.randrange(1, 181) == 180


if __name__ == '__main__':
    for _ in range(10):
        simulation(3600, 5)  # about 20 tasks

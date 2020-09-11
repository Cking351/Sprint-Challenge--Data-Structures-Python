class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.counter = 0

    def append(self, item):
        # Check if we can append to current capacity
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.counter] = item
            self.counter = self.counter + 1
        if self.counter >= self.capacity:
            self.counter = 0

    def get(self):
        return self.storage

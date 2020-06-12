class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldestItem = 0


    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.oldestItem] = item
            if self.oldestItem < len(self.storage) -1:
                self.oldestItem += 1
            else:
                self.oldestItem = 0

            # self.cur = (self.cur+1) % self.capacity

    def get(self):
        return self.storage

class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.indices = {}

    def insert(self, val):
        if val in self.indices:
            return False
        self.indices[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val) :
        if val not in self.indices:
            return False
        id = self.indices[val]
        self.num[id] = self.nums[-1]
        self.indices[self.num[id]] = id
        self.nums.pop()
        del self.indices[val]
        return True

    def getRandom(self):
        return choice(self.nums)

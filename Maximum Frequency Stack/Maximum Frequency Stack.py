from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.max_freq = 0

    def push(self, val):
        self.freq[val] += 1
        current_f = self.freq[val]

        if current_f > self.max_freq:
            self.max_freq = current_f

        self.group[current_f].append(val)

    def pop(self):
        val = self.group[self.max_freq].pop()

        self.freq[val] -= 1

        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Stack:

    def __init__(self):
        self.top_node = None

    def push(self, data):
        self.top_node = Node(data, self.top_node)

    def pop(self):
        if self.is_empty():
            raise IndexError('empty stack')
        data = self.top_node.data
        self.top_node = self.top_node.next
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError('empty stack')
        return self.top_node.data

    def is_empty(self):
        return self.top_node is None


class MyQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x):
        self.s1.push(x)

    def pop(self):
        self._move_elements_if_needed()
        return self.s2.pop()

    def peek(self):
        self._move_elements_if_needed()
        return self.s2.peek()

    def empty(self):
        return self.s1.is_empty() and self.s2.is_empty()

    def _move_elements_if_needed(self):
        if self.s2.is_empty():
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

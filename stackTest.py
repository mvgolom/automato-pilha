from random import randint
import numpy as np


class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)


s = Stack()
for i in range(20):
    s.push(randint(0,999999))


x = s.pop
print x
print x
print s.size()

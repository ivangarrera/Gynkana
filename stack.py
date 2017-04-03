class Stack:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop()

    def is_empty(self):
        return self.elements == []

    def peek(self):
        return self.elements[len(self.elements)-1]

    def size(self):
        return len(self.elements)


class Node:
    def __init__(self, element):
        self.parent = None
        self.child = None
        self.element = element

    def get_parent(self):
        return self.parent

    def get_child(self):
        return self.child

    def get_element(self):
        return self.element

    def add_child(self, child):
        if self.child is None:
            self.child = []
        self.child.append(child)

    def get_children(self):
        if self.child is None:
            return None
        else:
            return iter(self.child)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.element == other.element
        return NotImplemented


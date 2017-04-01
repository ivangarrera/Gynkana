class NodeBinaryTree:
    def __init__(self, element):
        self.parent = None
        self.left = None
        self.right = None
        self.element = element

    def set_parent(self, parent):
        self.parent = parent

    def add_left(self, node):
        self.left = node

    def add_right(self, node):
        self.right = node

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_parent(self):
        return self.parent

    def get_element(self):
        return self.element

    def __eq__(self, other):
        if isinstance(other, NodeBinaryTree):
            return self.element == other.element
        return NotImplemented

    def __str__(self):
        return self.element[1]+" "


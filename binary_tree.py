import node_binary_tree

class BinaryTree:

    def __init__(self, root):
        if root is None:
            self.root = None
            self.size = 0
        else:
            self.root = root
            self.size = 1

    def add_root(self, element):
        if element is None:
            print("The tree has a root")
        node = node_binary_tree.NodeBinaryTree(element)
        self.root = node
        self.size = 1

    def add_root_node(self, node):
        self.add_root(node.element)

    def add_left(self, element1, element2):
        node1 = self.find(self.root, element1)
        node2 = self.find(self.root, element2)
        if node1.element is not None and node2.element is None:
            node2 = node_binary_tree.NodeBinaryTree(element2)
            node2.set_parent(node1)
            node1.add_left(node2)
            self.size += 1
        elif node1 is None:
            print("Element {0} is not in the tree. Is not possible to add"
                  " unconnected nodes.".format(element1))
        else:
            print("Element {0} is in the tree. Is not possible to add"
                  " another parent.".format(element2))

    def add_right(self, element1, element2):
        node1 = self.find(self.root, element1)
        node2 = self.find(self.root, element2)
        if node1.element is not None and node2.element is None:
            node2 = node_binary_tree.NodeBinaryTree(element2)
            node2.set_parent(node1)
            node1.add_right(node2)
            self.size += 1
        elif node1 is None:
            print("Element {0} is not in the tree. Is not possible to add"
                  " unconnected nodes.".format(element1))
        else:
            print("Element {0} is in the tree. Is not possible to add"
                  " another parent.".format(element2))

    def add_right_node(self, node1, node2):
        self.add_right(node1.element, node2.element)

    def add_left_node(self, node1, node2):
        self.add_left(node1.element, node2.element)

    def get_nodes(self):
        list = []
        list.add(self.root)
        self.iteratorTree(self.root, list)
        return iter(list)

    def get_root(self):
        return self.root

    def get_left(self, element):
        node = self.find(self.root, element)
        return node.get_left()

    def get_right(self, element):
        node = self.find(self.root, element)
        return node.get_right()

    def get_parent(self, element):
        node = self.find(self.root, element)
        if node is not None:
            return node.get_parent()
        else:
            print("Element {0} is not in the tree".format(element))

    def is_internal(self, element):
        node = self.find(self.root, element)
        if node is not None:
            return node.get_left() is not None or node.get_right() is not None
        else:
            print("Element {0} is not in the tree".format(element))

    def is_external(self, element):
        node = self.find(self.root, element)
        if node is not None:
            return node.get_left() is None and node.get_right() is None
        else:
            print("Element {0} is not in the tree".format(element))

    def is_root(self, element):
        node = self.find(self.root, element)
        if node is not None:
            return node.get_parent() is None
        else:
            print("Element {0} is not in the tree".format(element))

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def __str__(self):
        if self.size == 0:
            str = "The tree is empty"
        else:
            str = "[{0}]".format(self.printTree(self.root))
        return str

    def find(self, node, element):
        node2 = node_binary_tree.NodeBinaryTree(None)
        left = node.get_left()
        right = node.get_right()
        if node.element == element:
            node2 = node
        elif left is not None:
            node2 = self.find(left, element)
        if node2.element is None and right is not None:
            node2 = self.find(right, element)
        return node2

    def iterator_tree(self, node, list):
        left = node.get_left()
        right = node.get_right()
        if left is not None:
            list.add(left)
            self.iterator_tree(left, list)
        if right is not None:
            list.add(right)
            self.iterator_tree(right, list)

    def print_tree(self, node):
        str = node.__str__()
        bool1 = node.get_left() is not None
        bool2 = node.get_right() is not None
        if bool1 or bool2:
            str += "("
            if bool1:
                str += "{0}".format(self.print_tree(node.get_left()))
            else:
                str += "null"
            if bool2:
                str += ", {0}".format(self.print_tree(node.get_right()))
            else:
                str += ", null"
            str += ")"
        return str


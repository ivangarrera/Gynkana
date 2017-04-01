import node


class Tree:

    def __init__(self, element):
        if element is None:
            self.root = None
            self.size = 0
        else:
            self.root = element
            self.size = 1

    def add_root(self, element):
        if self.root is not None:
            print("The tree has a root")
        self.root = element
        self.size = 1

    def add_child(self, element1, element2):
        if self.root is None:
            print("The tree has not root.")
        n1 = self.find(self.root, element1)
        n2 = self.find(self.root, element2)
        if n1 is not None and n2 is None:
            n2 = node.Node(element1)
            n2.parent = n1
            n1.add_child(n2)
            self.size += 1
        elif n1 is None:
            print("Is not possible to add unconnected nodes.\n"
                  "Element {0} is not in the tree.".format(element1))
        else:
            print("Element {0} is already in the tree.".format(element2))

    def get_parent(self, element):
        node = self.find(self.root, element)
        if node is not None:
            return node.parent
        else:
            print("Element {0} is not in the tree".format(element))

    def get_node(self, element):
        return self.find(self.root, element)

    def get_children(self, element):
        n = self.find(self.root, element)
        if n is not None:
            return n.children
        else:
            print("Element {0} is not in the tree".format(element))

    def is_internal(self, element):
        n = self.find(self.root, element)
        if n is not None:
            return n.children is not None
        else:
            print("Element {0} is not in the tree".format(element))

    def is_external(self, element):
        n = self.find(self.root, element)
        if n is not None:
            return n.children is None
        else:
            print("Element {0} is not in the tree".format(element))

    def is_root(self, element):
        n = self.find(self.root, element)
        if n is not None:
            return n.parent is None
        else:
            print("Element {0} is not in the tree".format(element))

    def is_empty(self):
        return self.size == 0

    def find(self, root, element):
        children = root.get_children
        m = None
        if root == element:
            m = root
        elif children is not None:
            var = True
            for x in children and var:
                m = x.next()
                if m == element:
                    var = False
                else:
                    m = self.find(m, element)
                    if m is not None and m == element:
                        var = False
        return m

    def print_tree(self, node):
        str = node.__str__()
        children = node.get_children()
        if children is not None:
            str += "("
            for x in children:
                m = x.next()
                str += self.print_tree(m)
                if x.next:
                    str += ","
            str += ")"
        return str

    def __str__(self):
        if self.size == 0:
            str = "The tree is empty"
        else:
            str = "[{0}]".format(self.print_tree(self.root))
        return str





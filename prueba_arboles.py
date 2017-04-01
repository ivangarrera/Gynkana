#!/usr/bin/python3

import node_binary_tree
import binary_tree

def crear_arbol2():
    element1 = (1, "7")
    element2 = (2, "6")
    element3 = (3, "5")
    element4 = (4, "4")
    element5 = (5, "3")
    element6 = (6, "9")
    element7 = (7, "3")
    minus = (8, "-")
    times1 = (9, "*")
    times2 = (10, "*")
    over = (11, "/")
    plus1 = (12, "+")
    plus2 = (13, "+")

    _node1 = node_binary_tree.NodeBinaryTree(element1)
    _node2 = node_binary_tree.NodeBinaryTree(element2)
    _node3 = node_binary_tree.NodeBinaryTree(element3)
    _node4 = node_binary_tree.NodeBinaryTree(element4)
    _node5 = node_binary_tree.NodeBinaryTree(element5)
    _node6 = node_binary_tree.NodeBinaryTree(element6)
    _node7 = node_binary_tree.NodeBinaryTree(element7)
    _minus = node_binary_tree.NodeBinaryTree(minus)
    _times1 = node_binary_tree.NodeBinaryTree(times1)
    _times2 = node_binary_tree.NodeBinaryTree(times2)
    _over = node_binary_tree.NodeBinaryTree(over)
    _plus1 = node_binary_tree.NodeBinaryTree(plus1)
    _plus2 = node_binary_tree.NodeBinaryTree(plus2)


    tree = binary_tree.BinaryTree(None)
    tree.add_root_node(_minus)
    tree.add_left_node(_minus, _plus1)
    tree.add_right_node(_minus, _over)
    tree.add_left_node(_plus1, _node1)
    tree.add_right_node(_plus1, _times1)
    tree.add_left_node(_times1, _node2)
    tree.add_right_node(_times1, _node3)
    tree.add_left_node(_over, _plus2)
    tree.add_right_node(_over, _node7)
    tree.add_left_node(_plus2, _times2)
    tree.add_right_node(_plus2, _node6)
    tree.add_left_node(_times2, _node4)
    tree.add_right_node(_times2, _node5)
    return tree

def crear_arbol():
    element1 = (1, "3")
    element2 = (2, "4")
    element3 = (3, "*")
    element4 = (4, "5")
    element5 = (4, "+")

    node1 = node_binary_tree.NodeBinaryTree(element1)
    node2 = node_binary_tree.NodeBinaryTree(element2)
    node3 = node_binary_tree.NodeBinaryTree(element3)
    node4 = node_binary_tree.NodeBinaryTree(element4)
    node5 = node_binary_tree.NodeBinaryTree(element5)

    tree = binary_tree.BinaryTree(None)
    tree.add_root_node(node5)
    tree.add_left_node(node5, node1)
    tree.add_right_node(node5, node3)
    tree.add_left_node(node3, node2)
    tree.add_right_node(node3, node4)
    return tree


def evaluar_expresion(tree, node):
    result = 0
    if tree.is_external(node.element):
        result = int(node.element[1])
    else:
        op = node.element[1]
        left = evaluar_expresion(tree, tree.get_left(node.element))
        right = evaluar_expresion(tree, tree.get_right(node.element))
        if op == "+":
            result = left + right
        elif op == "-":
            result = left - right
        elif op == "*":
            result = left * right
        elif op == "/":
            result = left / right
    return result

def print_expression(tree, node):
    str = ""
    if tree.is_external(node.element):
        str = node.element[1]
    else:
        str += "("
        str += print_expression(tree, tree.get_left(node.element))
        str += node.element[1]
        str += print_expression(tree, tree.get_right(node.element))
        str += ")"
    return str

if __name__ == "__main__":
    tree = crear_arbol()
    tree2 = crear_arbol2()
    print("El valor de la expresión {0} es: \n{1}".format(print_expression(tree, tree.get_root()),
                                                          evaluar_expresion(tree, tree.get_root())))

    print("El valor de la expresión {0} es: \n{1}".format(print_expression(tree2, tree2.get_root()),
                                                          evaluar_expresion(tree2, tree2.get_root())))

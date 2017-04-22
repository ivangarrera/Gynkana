import tokenize
import re
from io import StringIO
import math
import stack
import node_binary_tree
import time

def split_ecuacion(cadena):
    list = []
    patron = re.compile("\s")
    tupla = patron.subn("", cadena)
    """ FROM HERE """
    for token in tokenize.generate_tokens(StringIO(tupla[0]).readline):
        if token[1]:
            list.append(token[1])
    """ TO HERE, copied from http://stackoverflow.com/questions/24042517/splitting-a-python-string-by-math-expressions """
    return list


def crear_arbol(expresion):
    list = split_ecuacion(expresion)
    salida = infijo_to_postfijo(list)
    elementos = []
    w = 0
    for i in salida:
        w += 1
        if i.isdigit():
            node = node_binary_tree.NodeBinaryTree((w, i))
            elementos.append(node)
        else:
            parent = node_binary_tree.NodeBinaryTree((w, i))
            parent.add_right(elementos.pop())
            parent.add_left(elementos.pop())
            elementos.append(parent)
    result = evaluar_expresion(elementos.pop())
    return result


def evaluar_expresion(node):
    result = 0
    if node.get_right() is None and node.get_left() is None:
        result = int(node.element[1])
    else:
        op = node.element[1]
        left = evaluar_expresion(node.get_left())
        right = evaluar_expresion(node.get_right())
        if op == "+":
            result = left + right
        elif op == "-":
            result = left - right
        elif op == "*":
            result = left * right
        elif op == "/":
            result = math.floor(left/right)
    return result


def print_expression(node):
    str = ""
    if node.left is None and node.right is None:
        str = node.element[1]
    else:
        str += "("
        str += print_expression(node.get_left())
        str += node.element[1]
        str += print_expression(node.get_right())
        str += ")"
    return str


def infijo_to_postfijo(expression):
    st = stack.Stack()
    salida = []
    for i in expression:
        times = 0
        if is_open_parenthesis(i):
            st.push(i)
        elif is_close_parenthesis(i):
            for x in st.elements:
                if not st.is_empty() and not is_open_parenthesis(st.peek()):
                    salida.append(st.pop())
                if not st.is_empty() and not is_operator(st.peek()) and is_parentesis_opuesto(i, st.peek()) \
                        and times < 1:
                    times += 1
                    st.pop()
        elif i == "*" or i == "/":
            st.push(i)
        elif i == "+" or i == "-":
            if st.is_empty():
                st.push(i)
            elif st.peek() == "+" or st.peek() == "-":
                st.push(i)
            elif is_open_parenthesis(st.peek()):
                st.push(i)
            elif st.peek() == "*" or st.peek() == "/":
                n_list = []
                while st.peek() == "*" or st.peek() == "/":
                    n_list.append(st.pop())
                st.push(i)
                for x in n_list:
                    st.push(x)
        else:
            salida.append(i)
    return salida


def is_open_parenthesis(character):
    if character == "(" or character == "[" or character == "{":
        return True
    else:
        False


def is_close_parenthesis(character):
    if character == ")" or character == "]" or character == "}":
        return True
    else:
        False


def is_operator(character):
    if character == "*" or character == "/" or character == "+" or character == "-":
        return True
    else:
        return False


def is_parentesis_opuesto(parentesis1, parentesis2):
    if (parentesis1 == "(" and parentesis2 == ")") or (parentesis1 == ")" and parentesis2 == "("):
        return True
    elif (parentesis1 == "[" and parentesis2 == "]") or (parentesis1 == "]" and parentesis2 == "["):
        return True
    elif (parentesis1 == "{" and parentesis2 == "}") or (parentesis1 == "}" and parentesis2 == "{"):
        return True
    else:
        return False


def recv_all_data(socket, timeout):
    """ EXTRACTED FROM http://www.binarytides.com/receive-full-data-with-the-recv-socket-function-in-python/"""
    totaldata = []
    socket.setblocking(0)
    begin = time.time()
    while 1:
        if totaldata and time.time() - begin > timeout:
            break
        try:
            data = socket.recv(1600)
            if data:
                totaldata.append(data.decode())
                begin = time.time()
            else:
                time.sleep(0.001)
        except:
            pass
    return "".join(totaldata)
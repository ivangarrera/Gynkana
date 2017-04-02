#!/usr/bin/python3
# _*_ mode:python; coding:utf-8; tab-width:4 _*_

import sys
import socket
import node_binary_tree
import binary_tree
import struct
import re
import tokenize
from io import StringIO
import math

addr_uclm_server = ('atclab.esi.uclm.es', 2000)
secret_connexion_number = 0
port = 0


def step0():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = ('atclab.esi.uclm.es', 2000)

    sock.connect(address)

    data = sock.recv(1600).decode()
    vector = data.split('\n')
    global secret_connexion_number
    secret_connexion_number = vector[0]
    print(data)

    sock.close()


def step1():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('', 50000)
    sock.bind(server_address)

    msg = str(secret_connexion_number) + " 50000"
    sock.sendto(msg.encode(), addr_uclm_server)
    data, information = sock.recvfrom(1600)
    global port
    vector = data.decode().split("\n")
    port = int(vector[0])
    print(data.decode())
    sock.close()


def step2():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mathematical_server = ("atclab.esi.uclm.es", port)
    sock.connect(mathematical_server)

    while(1):
        data = sock.recv(1600)
        print(data.decode())
        var = split_ecuacion(data.decode())
        if var[0] != "(" and var[0] != "[" and var[0] != "{" and var[0] != "ERROR":
            break
        result = int(crear_arbol(data.decode()))
        string = "("+str(result)+")"
        print("Result is {0}".format(result))
        sock.sendall(string.encode())

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
    print(salida)
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
    pila = []
    salida = []
    for i in expression:
        times = 0
        if i == "(" or i == "[" or i == "{":
            pila.append(i)
        elif i == ")" or i == "]" or i == "}":
            for x in pila:
                if pila != [] and pila[len(pila)-1] != "(" and pila[len(pila)-1] != "[" and pila[len(pila)-1] != "{":
                    salida.append(pila.pop())
                if pila != [] and pila[len(pila)-1] != "+" and pila[len(pila)-1] != "-" and pila[len(pila)-1] != "*"\
                        and pila[len(pila)-1] != "/" and is_parentesis_opuesto(i, pila[len(pila)-1]) and times < 1:
                    times += 1
                    pila.pop()
        elif i == "*" or i == "/":
            pila.append(i)
        elif i == "+" or i == "-":
            if pila == []:
                pila.append(i)
            elif pila[len(pila)-1] == "+" or pila[len(pila)-1] == "-":
                pila.append(i)
            elif pila[len(pila)-1] == "(" or pila[len(pila)-1] == "[" or pila[len(pila)-1] == "{":
                pila.append(i)
            elif pila[len(pila)-1] == "*" or pila[len(pila)-1] == "/":
                n_list = []
                while pila[len(pila) - 1] == "*" or pila[len(pila) - 1] == "/":
                    n_list.append(pila.pop())
                pila.append(i)
                for x in n_list:
                    pila.append(x)
        else:
            salida.append(i)
    return salida

def is_parentesis_opuesto(parentesis1, parentesis2):
    if (parentesis1 == "(" and parentesis2 == ")") or (parentesis1 == ")" and parentesis2 == "("):
        return True
    elif (parentesis1 == "[" and parentesis2 == "]") or (parentesis1 == "]" and parentesis2 == "["):
        return True
    elif (parentesis1 == "{" and parentesis2 == "}") or (parentesis1 == "}" and parentesis2 == "{"):
        return True
    else:
        return False

if __name__ == "__main__":
    step0()
    step1()
    step2()

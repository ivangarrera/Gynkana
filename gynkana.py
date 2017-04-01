#!/usr/bin/python3
# _*_ mode:python; coding:utf-8; tab-width:4 _*_

import sys
import socket
import node_binary_tree
import binary_tree
import struct
import re

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

    data = sock.recv(1600)
    print(data.decode())


def crear_arbol(expresion):
    list = []
    for i in re.split(r'(\d+|\W+)', expresion):
        if i:
            list.append(i)
    print(list.__str__())

def postorder_algorithm(node):
    if node.element is not None:
        postorder_algorithm(node.get_left())
        postorder_algorithm(node.get_right())

if __name__ == "__main__":
    step0()
    step1()
    step2()

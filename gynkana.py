#!/usr/bin/python3
# _*_ mode:python; coding:utf-8; tab-width:4 _*_

import socket
import gynkana_operations
import httplib2
import struct

addr_uclm_server = ('atclab.esi.uclm.es', 2000)


def step0():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = ('atclab.esi.uclm.es', 2000)

    sock.connect(address)

    data = sock.recv(1600).decode()
    vector = data.splitlines()
    secret_connexion_number = vector[0]
    print(data)

    sock.close()
    return secret_connexion_number


def step1(secret_connexion_number):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('', 50000)
    sock.bind(server_address)

    msg = str(secret_connexion_number) + " 50000"
    sock.sendto(msg.encode(), addr_uclm_server)
    data, information = sock.recvfrom(1600)
    sock.close()
    return int(data.decode().splitlines()[0])


def step2(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mathematical_server = ("atclab.esi.uclm.es", port)
    sock.connect(mathematical_server)

    while 1:
        data = sock.recv(1600)
        print(data.decode())
        var = gynkana_operations.split_ecuacion(data.decode())
        if var[0] != "(" and var[0] != "[" and var[0] != "{" and var[0] != "ERROR":
            break
        result = int(gynkana_operations.crear_arbol(data.decode()))
        string = "({0})".format(result)
        print("Result is {0}".format(result))
        sock.sendall(string.encode())

    sock.close()
    return data.decode().splitlines()[0]


def step3(download_file_number):
    file_url = "http://atclab.esi.uclm.es:5000/{}".format(download_file_number)
    """ FROM HERE """
    h = httplib2.Http(".cache")
    resp, content = h.request(file_url, "GET")
    """ TO HERE, copied from: https://github.com/jcgregorio/httplib2/wiki/Examples-Python3 """
    print(content.decode())
    icmp_data = content.decode().splitlines()[0]

    return icmp_data


def step4(icmp_data):
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW,
                         socket.getprotobyname("icmp"))
    payload = icmp_data
    echo_icmp_type = 8
    echo_icmp_code = 0
    icmp_packet = struct.pack("!BBH", echo_icmp_type, echo_icmp_code, 0) + payload
    sock.sendto(icmp_packet, addr_uclm_server)

if __name__ == "__main__":
    secret_connexion_number = step0()
    port = step1(secret_connexion_number)
    download_file_number = step2(port)
    icmp_data = step3(download_file_number)
    step4(icmp_data)
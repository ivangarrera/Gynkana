#!/usr/bin/python3
# _*_ mode:python; coding:utf-8; tab-width:4 _*_

import socket
import gymkhana_operations
import httplib2
import struct
import icmp_checksum
import time


class Gymkhana:

    def __init__(self):
        init = True

    def step0(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        address = ('atclab.esi.uclm.es', 2000)

        sock.connect(address)

        data = sock.recv(1600).decode()
        vector = data.splitlines()
        secret_connexion_number = vector[0]
        print(data)

        sock.close()
        return secret_connexion_number

    def step1(self, secret_connexion_number):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address = ('', 50000)
        sock.bind(server_address)
        address = ('atclab.esi.uclm.es', 2000)

        msg = str(secret_connexion_number) + " 50000"
        sock.sendto(msg.encode(), address)
        data, information = sock.recvfrom(1600)
        print(data.decode())
        sock.close()
        return int(data.decode().splitlines()[0])

    def step2(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mathematical_server = ("atclab.esi.uclm.es", port)
        sock.connect(mathematical_server)

        while 1:
            data = gymkhana_operations.recv_all_data(sock, 0.3)
            print(data)
            var = gymkhana_operations.split_ecuacion(data)
            if not gymkhana_operations.is_open_parenthesis(var[0]) and var[0] != "ERROR":
                break
            result = int(gymkhana_operations.crear_arbol(data))
            string = "({})".format(result)
            print("Result is {}".format(result))
            sock.sendall(string.encode())

        sock.close()
        return data.splitlines()[0]

    def step3(self, download_file_number):
        file_url = "http://atclab.esi.uclm.es:5000/{}".format(download_file_number)
        """ FROM HERE """
        h = httplib2.Http(".cache")
        resp, content = h.request(file_url, "GET")
        """ TO HERE, copied from: https://github.com/jcgregorio/httplib2/wiki/Examples-Python3 """
        print(content.decode())
        icmp_data = content.decode().splitlines()[0]

        return icmp_data

    def step4(self, icmp_data):
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW,
                             socket.getprotobyname("icmp"))
        echo_icmp_type = 8
        echo_icmp_code = 0
        timestamp = time.strftime("%H:%M:%S")
        payload = "{} {}".format(timestamp, icmp_data).encode()
        icmp_packet = struct.pack("!BBHHH{}s".format(len(payload))
                                  , echo_icmp_type, echo_icmp_code, 0, 0, 1, payload)
        chk = icmp_checksum.cksum(icmp_packet)
        icmp_packet = struct.pack("!BBHHH{}s".format(len(payload))
                                  , echo_icmp_type, echo_icmp_code, chk, 0, 1, payload)
        sock.sendto(icmp_packet, ("atclab.esi.uclm.es", 2000))
        reply = sock.recv(1600)
        data = sock.recv(1600)
        (echo_icmp_type,
         echo_icmp_code,
         checksum,
         x,
         y,
         data) = struct.unpack("!bbHHH{}s".format(len(data[8:])), data)
        first_line = str(data.splitlines()[0]).replace("'", "")
        code = int(first_line.split(":")[2][2:])
        print(code)
        enunciado5step = data.splitlines()[1:]
        for i in enunciado5step:
            print(i.decode())
        return code

g = Gymkhana()
secret_connexion_number = g.step0()
port = g.step1(secret_connexion_number)
download_file_number = g.step2(port)
icmp_data = g.step3(download_file_number)
ss = g.step4(icmp_data)
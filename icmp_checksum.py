#!/usr/bin/python3
"""Calc checksum for all sniffed ICMP packages"""

# Copyright (C) 2009, 2014  David Villa Alises

import struct

def cksum(data):

    def sum16(data):
        """sum all the the 16-bit words in data"""
        if len(data) % 2:
            data += '\0'
        return sum(struct.unpack("!{}H".format(int(len(data) / 2)), data))

    retval = sum16(data)                       # sum
    retval = sum16(struct.pack('!L', retval))  # one's complement sum
    retval = (retval & 0xFFFF) ^ 0xFFFF        # one's complement
    return retval



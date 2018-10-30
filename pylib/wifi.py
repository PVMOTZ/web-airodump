"""
AP/Stations Classes
"""

class Device:

    def __init__(self):
        self.mac = None

    def __eq__(self, other):

        return self.mac == other.mac


class AP(Device):

    def __init__(self, mac, ssid, channel):
        self.mac = mac
        self.ssid = ssid
        self.channel = channel


class Station(Device):

    def __init__(self, mac, name=None, ap=None):
        self.mac = mac
        self.name = name
        self.ap = ap


class Attacker:

    def __init__(self, src_mac, dst_mac, count=0):
        self.src_mac = src_mac
        self.dst_mac = dst_mac
        self.count = 0


    def __eq__(self, other):

        return (self.src_mac, self.dst_mac) == (other.src_mac, other.dst_mac)


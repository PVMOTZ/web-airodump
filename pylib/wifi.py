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




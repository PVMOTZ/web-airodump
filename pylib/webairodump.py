"""
Interface
"""
from pylib.mon import Monitoramento
from pylib.helper import interfaces_list, interface_mode

"""
Fachada Web-AiroDump
"""
class Wairodump():

    def __init__(self):
        self.mon = Monitoramento()

    def get_wireless_list(self):
        """
        get a list with the wireless interfaces up
        :return: string list
        """
        ilist = interfaces_list()

        return ilist

    def get_aps(self):
        """
        Return a dict d with aps mac, where d[mac] = ap information
        :return:
        """

        return self.mon.get_aps()

    def get_stations(self, ap=None):
        """
        Return a dict d with aps mac, where d[mac] = ap information
        :return:
        """

        return self.mon.get_stations()


    def start_monitoring(self, interface):
        """
        Start listening at interface
        """
        self.mon.start(interface)

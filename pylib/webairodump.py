"""
Interface
"""
from pylib.classes import Monitoramento


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
        #"duck"
        return ['wlp3s0mon']

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

    def get_aps_columns(self):
        aps = self.mon.get_aps()

        if aps:
            columns = aps[0]

            return list(columns.keys())
        else:
            return None

    def get_stations_columns(self):

        sts = self.mon.get_stations()

        if sts:
            columns = sts[0]

            return list(columns.keys())
        else:
            return None

    def start_monitoring(self, interface):
        """
        Start listening at interface
        """
        self.mon.start(interface)

"""
Interface
"""
from pylib.mon import Monitoramento

"""
Fachada Web-AiroDump
"""
class Wairodump():

    def __init__(self):
        self.mon = Monitoramento()

    def get_ap(self, bssid):

        return self.mon.get_ap(bssid)

    def get_aps(self):
        """
        Return a list with aps
        :return: [aps]
        """

        return self.mon.get_aps()

    def get_stations(self, ap=None):
        """
        Return a dict d with aps mac, where d[mac] = ap information
        :return:
        """

        return self.mon.get_stations()

    def get_attackers(self):

        return self.mon.get_attackers()

    def start_monitoring(self, interface):
        """
        Start listening at interface
        """
        self.mon.start(interface)

"""
Classes para guardar valores do Tshark
"""
import pyshark
from threading import Thread
from pylib.helper import *
from pylib.wifi import AP, Station, Attacker


class Monitoramento:

    def __init__(self):
        self.aps = {}
        self.stations = {}
        self.attackers = {}

    def get_ap(self, bssid):

        if bssid in self.aps:
            return self.aps[bssid]

    def get_aps(self):

        return list(self.aps.values())

    def get_stations(self):

        return list(self.stations.values())

    def get_attackers(self):

        return list(self.attackers.values())

    def start(self, interface):
        """
        Inicia o monitoramento atravez da interface
        """
        self.capture = pyshark.LiveCapture(interface=interface)
        self.capture.sniff_continuously(packet_count=50)

        # executando em thread
        t = Thread(target=self.__start, args=(interface,))
        t.start()

    def __start(self, interface):
        """
        :param interface:
        :return: None
        """
        self.capture.apply_on_packets(self.__apply)

    def __apply(self, *args):
        """
        Essa função é aplicada a todos os pacotes lidos pela interface de captura
        Delegando cada pacote com relação com seu tipo
        """
        pkt = args[0]

        pkt_type = int(pkt.wlan.fc_type)

        if pkt_type == MANAGEMENT_FRAME:
            self.__managament_frame(pkt)
        elif pkt_type == CONTROL_FRAME:
            self.__control_frame(pkt)
        elif pkt_type == DATA_FRAME:
            self.__data_frame(pkt)
        else:
            pass ## Pacote não reconhecido

    def __managament_frame(self, pkt):
        pkt_info = pkt_simple_info_extractor(pkt)

        # Check beacon frame
        if pkt_info['subtype'] == BEACON:
            ssid  = pkt.layers[3].ssid
            channel  = pkt.wlan_radio.channel
            bssid = pkt.wlan.bssid

            if bssid not in self.aps:
                ap = AP(bssid, ssid, channel)

                self.aps[bssid] = ap

    def __control_frame(self, pkt):
        # Se existe dados sendo transmitidos dos APs para as estações
        try:
            src_mac = pkt.wlan.sa
            dst_mac = pkt.wlan.da

            self.__process(src_mac, dst_mac)
        except:
            pass

    def __data_frame(self, pkt):
        # Se existe dados sendo transmitidos dos APs para as estações
        try:
            src_mac = pkt.wlan.sa
            dst_mac = pkt.wlan.da

            self.__process(src_mac, dst_mac)
        except:
            pass

    def __process(self, src_mac, dst_mac):

        if src_mac in self.aps and dst_mac != 'ff:ff:ff:ff:ff:ff': # Origem AP -  Destino ST

            if dst_mac not in self.stations:
                station = Station(mac=dst_mac, ap=src_mac)
                self.stations[dst_mac] = station
            else:
                self.stations[dst_mac].ap = src_mac

            if (dst_mac, src_mac) in self.attackers:
                del self.attackers[(dst_mac, src_mac)]

        elif dst_mac in self.aps and src_mac not in self.stations: # Checando por ataques

            if (src_mac, dst_mac) in self.attackers:
                self.attackers[(src_mac, dst_mac)].count += 1
            else:
                att = Attacker(src_mac, dst_mac, 1)

                self.attackers[(src_mac, dst_mac)] = att
        else: # pacote não processado
            pass

    def clear(self):
        self.attackers.clear()
        self.aps.clear()
        self.stations.clear()

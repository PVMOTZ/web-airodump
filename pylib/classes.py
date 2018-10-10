"""
Classes para guardar valores do Tshark
"""
import pyshark
import time
from threading import Thread
from pylib.helper import *

class Monitoramento:

    def __init__(self):
        self.aps = {}
        self.stations = {}
        self.connections = {}
        self.capture = None

    def get_aps(self):
        aps_list = []

        for a in self.aps:
            aps_list.append(self.aps[a])

        return aps_list

    def get_stations(self):

        stations_list = []

        for a in self.stations:
            stations_list.append(self.stations[a])

        return stations_list

    def start(self, interface):
        """
        Inicia o monitoramento atravez da interface
        """
        self.capture = pyshark.LiveCapture(interface=interface)
        self.capture.sniff_continuously(packet_count=1)

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

        pkt_info = pkt_simple_info_extractor(pkt)
        pkt_type = pkt_info['type']


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
            ap_info = ap_info_extractor(pkt)
            ap_bssid = ap_info['bssid']

            self.aps[ap_bssid] = ap_info


    def __control_frame(self, pkt):
        pass


    def __data_frame(self, pkt):
        pkt_info = pkt_simple_info_extractor(pkt)

        # Se existe dados sendo transmitidos dos APs para as estações
        if pkt_info['subtype'] == 40:

            pkt_data_info = data_info_extractor(pkt)

            if pkt_data_info['ta'] in self.aps:
                if pkt_data_info['da'] not in self.stations:
                    self.stations[pkt_data_info['da']] = {'mac' : pkt_data_info['da'],'conectado' : pkt_data_info['ta']}

    def clear(self):
        pass

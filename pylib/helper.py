"""
Temporario Helper.py
"""

"""
WLAN constantes para TYPE/SUBTYPE 
"""
# Managent Frames
MANAGEMENT_FRAME = 0

# Subtypes
ASSOCIATION_REQUEST = 0
ASSOCIATION_RESPONSE = 1
RESSOCIATION_REQUEST = 2
RESSOCIATION_RESPONSE = 3
PROBE_REQUEST = 4
PROBE_RESPONSE = 5
BEACON = 8
ATIM = 9
DISASSOCIATE = 10
AUTHENTICATION = 11
DEAUTHENTICATION = 12

# Control Frame
CONTROL_FRAME = 1

# Subtypes
PS_POLL = 26
RTS = 27
CTS = 28
ACK = 29

# Data Frames
DATA_FRAME = 2

# Subtypes
NULL_DATA = 36

"""
PyShark PKT Helper Extractor
"""
def pkt_simple_info_extractor(pkt):

	ref = {}

	ref['type'] = int(pkt.wlan.fc_type)
	ref['subtype'] = int(pkt.wlan.fc_type_subtype)

	return ref


def pkt_radio_info_extractor(pkt):
	"""
	Dado um pacote WLAN, retorna um dicionario contendo os labels:

	channel
  	frequency
  	signal
  	data_rate
  	phy
	"""

	ref = {}

	ref['channel']  = pkt.wlan_radio.channel
	ref['frequency']= pkt.wlan_radio.frequency
	ref['signal'] = pkt.wlan_radio.signal_dbm
	#ref['data_rate']= pkt.wlan_radio.data_rate
	#ref['phy']   = pkt.wlan_radio.phy

	return ref


def ap_info_extractor(pkt):
	"""
 	Dado um pacote WLAN, retorna um dicionario contendo os labels:

  	bssid
  	type
  	subtype
  	addr
  	ssid
	"""

	ref = {} 
	ref['bssid']  = pkt.wlan.bssid
	ref['ssid']  = pkt.layers[3].ssid

	# adicionando dados de radio
	radio_info = pkt_radio_info_extractor(pkt)
	ref.update(radio_info)

	return ref


def data_info_extractor(pkt):
    """
    labels:
    """

    ref = {}

    ref['sa'] = pkt.wlan.sa
    ref['da'] = pkt.wlan.da
    ref['ta'] = pkt.wlan.ta
    ref['ra'] = pkt.wlan.ra
    ref['type'] = int(pkt.wlan.fc_type)
    ref['subtype'] = int(pkt.wlan.fc_type_subtype)

    return ref



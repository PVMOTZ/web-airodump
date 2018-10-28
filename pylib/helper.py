"""
Temporario Helper.py
"""
"""
PyShark PKT Helper Extractor
"""
def pkt_simple_info_extractor(pkt):

	ref = {}

	ref['type'] = int(pkt.wlan.fc_type)
	ref['subtype'] = int(pkt.wlan.fc_type_subtype)

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

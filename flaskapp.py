"""
Main Flask File
"""
import sys
from pylib.webairodump import Wairodump
from flask import render_template
from flask import Flask

# Start Mon Object
interface_name = sys.argv[1]
web_mon = Wairodump()
web_mon.start_monitoring(interface_name)

# Iniciar App Flask
app = Flask(__name__)

@app.route("/")
def mon(interface=None):
    # get aps
    all_aps = web_mon.get_aps()
    sts = web_mon.get_stations()
    att = web_mon.get_attackers()

    aps = [ap for ap in all_aps if ap.ssid != "SSID: "]
    hiddens_aps = [ap for ap in all_aps if ap.ssid == "SSID: "]

    return render_template("mon.html",  aps = aps,
                                        hiddens_aps = hiddens_aps,
                                        stations = sts,
                                        attackers = att)

@app.route("/ap/<bssid>")
def mon_target(bssid):
    # get aps
    ap = web_mon.get_ap(bssid)
    sts = web_mon.get_stations()
    atts = web_mon.get_attackers()

    # filtrando estações
    stations = [st for st in sts if st.ap == bssid]
    attackers = [att for att in atts if att.dst_mac == bssid]

    # filtrando atacantes
    return render_template("mon_target.html",  ap = ap,
                                        stations = stations,
                                        attackers = attackers)

app.run(debug=True, use_reloader=True)

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
    aps = web_mon.get_aps()
    sts = web_mon.get_stations()

    return render_template("mon.html",  aps = aps,
                                        stations = sts)


@app.route("/mon/ap/<bssid>")
def mon_target(bssid):
    # get aps
    ap = web_mon.get_ap(bssid)
    sts = web_mon.get_stations()

    stations = []
    for st in sts:
        if st.ap == bssid:
            stations.append(st)

    return render_template("mon_target.html",  ap = ap,
                                        stations = stations)

app.run(debug=True, use_reloader=True)

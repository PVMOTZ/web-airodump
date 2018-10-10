"""
Main Flask File
"""
from pylib.webairodump import Wairodump
from flask import render_template
from flask import Flask

# WebAirodump
web_mon = Wairodump()
web_mon.start_monitoring('wlp3s0mon')

# Iniciando App
app = Flask(__name__)

@app.route("/")
def home():

    wlist = web_mon.get_wireless_list()

    return render_template("wireless_list.html", wlist=wlist)

@app.route("/mon")
def mon():
    aps = web_mon.get_aps()
    sts = web_mon.get_stations()

    aps_columns = web_mon.get_aps_columns()
    sts_columns = web_mon.get_stations_columns()

    return render_template("mon.html",  aps = aps,
                                        sts = sts,
                                        aps_columns=aps_columns,
                                        sts_columns=sts_columns)

app.run(debug=True, use_reloader=True)

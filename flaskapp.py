"""
Main Flask File
"""
from pylib.webairodump import Wairodump
from pylib.helper import interfaces_list
from flask import render_template
from flask import Flask

# start mon at interface
web_mon = Wairodump()
web_mon.start_monitoring('wlp3s0mon')

# Iniciando App
app = Flask(__name__)

@app.route("/")
def home():

    wlist = interfaces_list

    return render_template("wireless_list.html", wlist=wlist)

@app.route("/mon/")
def mon():
    #
    aps = web_mon.get_aps()
    sts = web_mon.get_stations()

    return render_template("mon.html",  aps = aps,
                                        stations = sts)

app.run(debug=True, use_reloader=True)

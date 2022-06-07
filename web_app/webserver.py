#!/usr/bin/env python3

# 必要なライブラリをインポート
import subprocess
import datetime
from flask import Flask, render_template, send_from_directory, request
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = "AIKitKey"

socketio = SocketIO(app, cors_allowed_origins="*")


@app.route("/")
def root():
    return render_template("index.html")

@socketio.on("connect")
def connect(auth):
    print("Connected.")

@socketio.on("disconnect")
def disconnect():
    print("Disconnect.")

@socketio.on("temp_update_request")
def temp_update_request(json):
    read_temp = int(subprocess.run("cat /sys/class/thermal/thermal_zone0/temp", shell=True, encoding='utf-8', stdout=subprocess.PIPE).stdout)   
    temp = "{:.1f}".format(int(read_temp) / 1000.0)
    date = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9), "JST")).strftime('%Y年%m月%d日 %H時%M分%S秒')
    emit("temp_update", {"temp": temp, "date": date}, broadcast=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
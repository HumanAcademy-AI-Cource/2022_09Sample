#!/usr/bin/env python3

# 必要なライブラリをインポート
import subprocess
import datetime

# RaspberryPiの温度情報を取得
read_temp = int(subprocess.run("cat /sys/class/thermal/thermal_zone0/temp", shell=True, encoding='utf-8', stdout=subprocess.PIPE).stdout)
# 取得した温度情報は1000倍された数値なので、1000で割って元に戻す
temp = "{:.1f}".format(int(read_temp) / 1000.0)
# 現在時刻を取得
date = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9), "JST"))
ymd = date.strftime("%Y/%m/%d")
hms = date.strftime("%H:%M:%S")

# 時刻と温度を端末に表示
print("({} {}) {}℃".format(ymd, hms, temp))
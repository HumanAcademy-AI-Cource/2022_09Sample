#!/usr/bin/env python3

# 必要なライブラリをインポート
import subprocess
import datetime
import csv
import time
import os
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rc('font', family='Noto Sans CJK JP')
os.environ["QT_LOGGING_RULES"] = "*=false"

# 読み出したデータを保持する配列
date_list = []
temp_list = []


# 指定回数だけ実行する
for index in range(10):
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
    # CSVにデータを追記する
    date_list.append(hms)
    temp_list.append(temp)
    
    # 指定した秒数待つ
    time.sleep(1)

# グラフを描画するための設定
plt.xticks(rotation=30)
plt.xlabel("-取得時刻-")
plt.ylabel("-ラズパイ温度-")
plt.subplots_adjust(left=0.1, right=0.90, bottom=0.27, top=0.9)

# グラフを作成
graph = plt.plot(date_list, temp_list)
# グラフを画像にして保存
plt.savefig("temp_graph.png")
print("ラズパイの温度グラフを作成しました。")

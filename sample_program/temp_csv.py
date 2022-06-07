#!/usr/bin/env python3

# 必要なライブラリをインポート
import subprocess
import datetime
import csv
import time

# CSVとして保存するファイルを作成
with open("temp_data.csv", "w") as f:
    # CSVを作成する準備
    writer = csv.writer(f)
    # CSVにヘッダーを追加
    writer.writerow(["日付","時刻","温度"])
    
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
        writer.writerow([ymd, hms, temp])
        
        # 指定した秒数待つ
        time.sleep(1)
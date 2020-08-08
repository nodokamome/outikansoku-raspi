#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import bme280_custom
import datetime
import requests
import threading

from dotenv import load_dotenv

from web import uploadSensorValues
from led import flash_led

#.env取得
load_dotenv()

#環境変数から取得
led_start_hour_url = os.getenv("LED_START_HOUR_URL")
led_end_hour_url = os.getenv("LED_END_HOUR_URL")
dt_now = datetime.datetime.now()

#LED点滅開始時間の取得
response = requests.get(led_start_hour_url)
led_start_hour=int(response.text);
#LED点滅終了時間の取得
response = requests.get(led_end_hour_url)
led_end_hour=int(response.text);

#センサー値をカンマ区切りで取得
csv = bme280_custom.readData()
list = csv.split(",")
 
#カンマ区切りを別々の変数に格納
#press = list[0]   #気圧（見ても分からないのでアップしない）
temp = list[1]    #室温
hum = list[2]     #湿度
 
#webへPOSTする
response = uploadSensorValues(temp,hum)

#POST時に点滅時間外ならLED点滅無し
if led_start_hour <= dt_now.hour:
        if dt_now.hour <= led_end_hour:
                #青は通信の確認用。良い状態のときだけ緑点滅。それ以外は赤
                if response != '':
                        flash_led("blue")
                if response == u'先輩！お部屋が最高の状態です！快適で仕事がはかどります！！':
                        flash_led("green")
                else:
                        flash_led("red")

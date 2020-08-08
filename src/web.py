#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import urllib3
import requests
import json

from dotenv import load_dotenv

from led import flash_led
from datetime import datetime

#.envを取得
load_dotenv()

#環境変数から取得
token = os.getenv("TOKEN") 
url = os.getenv("SYSTEM_URL")
#SSLのWarningを非表示
urllib3.disable_warnings()

#日時、室温、湿度、トークン情報をアップ
def uploadSensorValues(temp, hum):

    sensorsdata = {'datetime':datetime.now().strftime("%Y/%m/%d %H:%M:%S"),'temp':temp,'hum':hum, 'token':token}
    print json.dumps(sensorsdata)

    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(sensorsdata), headers=headers, verify=False)
    #送信情報と、Webでの設定から判断結果を呼び出し元に返す
    return response.text

#以下、デバッグ用
def main():
    uploadSensorValues(21.8, 39.1)

if __name__ == '__main__':
    main()

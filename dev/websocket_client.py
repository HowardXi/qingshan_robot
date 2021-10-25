#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Xi WenHao
# @Email    : xiwenhao1994@gmail.com
# @Project  : qingshan
# @Time     : 2021/10/25 10:37
# @File     : websocket_client.py

import websocket
import json
from query.common_query import query_macro
from requests import post


def on_message(ws, message):
    msg = json.loads(message)
    if "message_type" in msg and msg["message_type"] == "group":
        print(message)

    if msg["message"] == "宏 冰心":
        result = query_macro("冰心诀")
        print(result)
        res = post("http://192.168.189.133:15700/send_group_msg", json={
            "group_id": 556425258,
            "message": "msg from bot",
            "auto_escape": False
        })
        print (res, res.content)

def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")



if __name__ == "__main__":
    # websocket.enableTrace(True)
    host = "ws://192.168.189.133:16700/"
    ws = websocket.WebSocketApp(host,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()
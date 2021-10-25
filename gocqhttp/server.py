#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Xi WenHao
# @Email    : xiwenhao1994@gmail.com
# @Project  : qingshan
# @Time     : 2021/10/25 14:50
# @File     : server.py
import websocket
import json
from settings import cfg
from query.common_query import query_macro, query_heighten
from query.static import query_saohua, flatterer_diary
from gocqhttp.action.send_msg import send_group_msg
from match.xinfa import xinfa_set, match_xinfa
from loguru import logger


def on_message(ws, message):
    msg = json.loads(message)
    if "message_type" not in msg or msg["message_type"] not in ("group", ):
        return
    op = msg["message"].split(" ")[0]
    args = msg["message"].split(" ")[1:]

    if op == "宏":
        if args in xinfa_set:
            result = query_macro(match_xinfa(args))
            logger.info(f"query macro: {args} result: {result}")
            send_group_msg(msg["group_id"], result)

    if op == "小药":
        result = query_heighten(match_xinfa("冰心"))
        send_group_msg(msg["group_id"], f"[CQ:image,file={result},id=40000]")

    if op == "来句骚话":
        send_group_msg(msg["group_id"], query_saohua())

    if op == "舔狗日记":
        send_group_msg(msg["group_id"], flatterer_diary())


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")

ws = websocket.WebSocketApp(cfg["gocqhttp"]["ws_addr"],
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)


# if __name__ == "__main__":
#     # websocket.enableTrace(True)
#     host = "ws://192.168.189.133:16700/"
#     ws = websocket.WebSocketApp(host,
#                                 on_message=on_message,
#                                 on_error=on_error,
#                                 on_close=on_close)
#     ws.run_forever()
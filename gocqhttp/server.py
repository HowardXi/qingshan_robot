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
from query.static import query_saohua, flatterer_diary, random_image
from gocqhttp.action.send_msg import send_group_msg
from match.xinfa import xinfa_set, match_xinfa
from loguru import logger


def on_message(ws, message):
    msg = json.loads(message)
    if "message_type" not in msg or msg["message_type"] not in ("group",):
        return
    op = msg["message"].split(" ")[0]
    args = msg["message"].split(" ")[1:]

    if op == "宏":
        if args[-1] in xinfa_set:
            result = query_macro(match_xinfa(args[-1]))
            logger.info(f"query macro: {args} result: {result}")
            send_group_msg(msg["group_id"], result)

    if op == "小药":
        image_ref = query_heighten(match_xinfa("冰心"))
        send_group_msg(msg["group_id"],
                       f"[CQ:image,file={image_ref},id=40000]")

    if op == "来张美图":
        image_ref = random_image()
        send_group_msg(msg["group_id"],
                       f"[CQ:image,file={image_ref},id=40000]")

    if op == "来句骚话":
        send_group_msg(msg["group_id"], query_saohua())

    if op == "舔狗日记":
        send_group_msg(msg["group_id"], flatterer_diary())


def on_error(ws, error):
    logger.error(error)


def on_close(ws):
    logger.warning("websocket closed.")


ws = websocket.WebSocketApp(
    cfg["gocqhttp"]["ws_addr"],
    on_message=on_message,
    on_error=on_error,
    on_close=on_close)

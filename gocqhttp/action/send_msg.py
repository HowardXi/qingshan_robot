#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Xi WenHao
# @Email    : xiwenhao1994@gmail.com
# @Project  : qingshan
# @Time     : 2021/10/25 14:49
# @File     : send_msg.py

from requests import get, post
from settings import cfg
from loguru import logger

base_addr = cfg["gocqhttp"]["http_addr"]


def send_group_msg(group_id: int, msg: str, auto_escape=False):
    endpoint = "/send_group_msg"
    res = post(base_addr + endpoint, json={
        "group_id": group_id,
        "message": msg,
        "auto_escape": auto_escape
    })
    if res.status_code == 200:
        logger.info(f"send group msg {msg} to {group_id} success")
        return ""
    else:
        logger.error(
            f"send group msg {msg} to {group_id} error, reason: "
            f"{res.content}, code: {res.status_code}")
        return res.content


def send_private_msg():
    pass

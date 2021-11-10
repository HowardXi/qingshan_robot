#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Xi WenHao
# @Email    : xiwenhao1994@gmail.com
# @Project  : qingshan
# @Time     : 2021/11/9 16:59
# @File     : parse_msg.py

from loguru import logger

def cqcode_num(msg):
    return msg.count("[CQ")


def parse_cqcode(cq_msg):
    # [CQ:at,qq=10001000]
    cq_msg = cq_msg[1:-1]
    cq, *cq_datas = cq_msg.split(",", 1)
    type = cq.split(":")[-1]
    args = {}
    for cq_data in cq_datas:
        k, v = cq_data.split("=")
        args[k] = int(v) if v.isalnum() else v
    logger.info(f"parse CQ code: type={type}, args={args}")
    return {
        "type": type,
        "args": args
    }



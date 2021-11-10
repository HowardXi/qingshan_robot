#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Xi WenHao
# @Email    : xiwenhao@qianxin.com
# @Project  : qingshan
# @Time     : 2021/10/19 17:53
# @File     : main.py

from loguru import logger
from components.server_monitor import server_monitor
from threading import Thread

from gocqhttp.server import ws

if __name__ == '__main__':
    t = Thread(target=server_monitor)
    t.setDaemon(True)
    t.start()
    logger.info("---- main server start ----")
    ws.run_forever()

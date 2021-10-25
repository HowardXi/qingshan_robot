#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Xi WenHao
# @Email    : xiwenhao@qianxin.com
# @Project  : qingshan
# @Time     : 2021/10/19 17:53
# @File     : main.py

from loguru import logger

from gocqhttp.server import ws

if __name__ == '__main__':
    ws.run_forever()

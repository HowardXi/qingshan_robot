#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Xi WenHao
# @Email    : xiwenhao1994@gmail.com
# @Project  : qingshan
# @Time     : 2021/10/29 17:57
# @File     : exception.py

class QsBaseException(Exception):
    def __init__(self, group_id):
        self.group_id = group_id

class ServerNotFound(QsBaseException):
    def __str__(self):
        return "找不到这个服务器"

class ItemNotFound(QsBaseException):
    def __str__(self):
        return "找不到这个物品, 还没听说过"

if __name__ == '__main__':
    try:
        raise ServerNotFound(1234123)
    except Exception as e:
        print(e)
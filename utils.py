#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Xi WenHao
# @Email    : xiwenhao1994@gmail.com
# @Project  : qingshan
# @Time     : 2021/10/19 18:50
# @File     : utils.py

from importlib import import_module

__all__ = [
    "import_class"
]


def import_class(class_path):
    file_path, cls = class_path.split(":")
    return getattr(import_module(file_path), cls)



if __name__ == '__main__':
    m = import_class("message_server.mirai_http_ws.mirai:MiraiWSServer")
    print(dir(m))

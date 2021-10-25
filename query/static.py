#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Xi WenHao
# @Email    : xiwenhao1994@gmail.com
# @Project  : qingshan
# @Time     : 2021/10/25 16:12
# @File     : static.py

from requests import get, post
from query import base_url
import json

def query_saohua():
    endpoint = "/random"
    request = get(base_url + endpoint)
    if request.status_code == 200:
        data = request.json()["data"]
        return data["text"]
    else:
        return request
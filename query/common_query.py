#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Xi WenHao
# @Email    : xiwenhao1994@gmail.com
# @Project  : qingshan
# @Time     : 2021/10/25 11:09
# @File     : common_query.py

from requests import get, post
from query import base_url
import json


def query_macro(xinfa):
    endpoint = "/macro"
    request = get(base_url + endpoint, data=json.dumps({"name": xinfa}))
    if request.status_code == 200:
        data =  request.json()["data"]
        return "奇穴方案: " + data["qixue"] +"\r\n宏:\r\n"+ data["macro"]
    else:
        return request

def query_heighten(xinfa):
    endpoint = "/heighten"
    request = get(base_url + endpoint, data=json.dumps({"name": xinfa}))
    if request.status_code == 200:
        data = request.json()["data"]
        return data["url"]
    else:
        return request



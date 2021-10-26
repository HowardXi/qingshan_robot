#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Xi WenHao
# @Email    : xiwenhao1994@gmail.com
# @Project  : qingshan
# @Time     : 2021/10/25 16:12
# @File     : static.py

from requests import get, post
from query import jx3api_app, jx3api_share, image_gufeng, image_erciyuan
import json
from re import compile

find_jpg = compile(r"cdn.seovx.com/ha/img/.*?jpg")

def query_saohua():
    endpoint = "/random"
    request = get(jx3api_app + endpoint)
    if request.status_code == 200:
        data = request.json()["data"]
        return data["text"]
    else:
        return request

def flatterer_diary():
    endpoint = "/random"
    request = get(jx3api_share + endpoint)
    if request.status_code == 200:
        data = request.json()["data"]
        return data["text"]
    else:
        return request

def random_image(styly="gufeng"):
    r = get(image_gufeng)
    image_ref = find_jpg.findall(str(r.content))[0]
    return image_ref

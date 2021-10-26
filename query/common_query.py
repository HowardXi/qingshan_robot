#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Xi WenHao
# @Email    : xiwenhao1994@gmail.com
# @Project  : qingshan
# @Time     : 2021/10/25 11:09
# @File     : common_query.py

from requests import get, post
from query import jx3api_app
import json
import time


def query_macro(xinfa):
    endpoint = "/macro"
    request = get(jx3api_app + endpoint, data=json.dumps({"name": xinfa}))
    if request.status_code == 200:
        data =  request.json()["data"]
        return "奇穴方案: " + data["qixue"] +"\r\n宏:\r\n"+ data["macro"]
    else:
        return request

def query_heighten(xinfa):
    endpoint = "/heighten"
    request = get(jx3api_app + endpoint, data=json.dumps({"name": xinfa}))
    if request.status_code == 200:
        data = request.json()["data"]
        return data["url"]
    else:
        return request

def query_daily(server_name="天鹅坪"):
    # TODO unfinished
    endpoint = "/daily"
    if server_name == None:
        server_name = "天鹅坪"
    request = get(jx3api_app + endpoint, data=json.dumps({"name": server_name}))
    if request.status_code == 200:
        data = request.json()["data"]
        return f"""日期: {data["date"]} 周{data["week"]} 服务器: {server_name}
公共周长: {data["weekPublic"]}
五人周长: {data["weekFive"]}
团队周长: {data["weekTeam"]}
每日战场: {data["dayBattle"]}
大战:     {data["dayWar"]}
阵营日常: {data["dayCamp"]}
共同日常: {data["dayPublic"]}"""
    else:
        return request

def query_gold_price(server_name="天鹅坪"):
    endpoint = "/demon"
    if server_name == None:
        server_name = "天鹅坪"
    request = get(jx3api_app + endpoint, data=json.dumps({"server": server_name}))
    if request.status_code == 200:
        data = request.json()["data"]
        timestamp = time.localtime(data["time"])
        datetime = time.strftime("%Y-%m-%d %H:%M:%S", timestamp)
        return f"""更新时间: {datetime}  服务器: {data["server"]}
万宝楼:\t{data["wanbaolou"]}
贴吧:\t{data["tieba"]}
5173:\t{data["5173"]}"""
    else:
        return request

if __name__ == '__main__':
    print(query_gold_price())
    print(query_daily())
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Xi WenHao
# @Email    : xiwenhao1994@gmail.com
# @Project  : qingshan
# @Time     : 2021/11/10 18:13
# @File     : weather.py

import json
from requests import get
from query.utils import get_headers
from exception import QueryError
import xmltodict

API = "http://wthrcdn.etouch.cn/WeatherApi?citykey=%s"

def query_city_code(city:str):
    with open("db/weather_city.json", "r", encoding="utf-8") as f:
        city2code = json.load(f)
    if city not in city2code:
        raise QueryError
    else:
        return city2code[city]


def query_weather(city_code):
    r = get(API % city_code, headers=get_headers())
    if r.status_code != 200:
        raise QueryError
    return json.dumps(xmltodict.parse(r.content), ensure_ascii=False)


def weather_msg_format(weather_json):
    data = json.loads(weather_json)["resp"]
    today = data["forecast"]["weather"][0]
    msg = f"""{data["city"]}天气 更新时间: {data["updatetime"]}
今天 最{today["high"]} 最{today["low"]} 白天天气: {today["day"]["type"]} \
夜间天气: {today["night"]["type"]}
当前天气 温度: {data["wendu"]} 风力: {data["fengxiang"]}{data["fengli"]} \
湿度: {data["shidu"]}
预报:
"""
    for forecast in data["forecast"]["weather"][1:4]:
        msg += f"""{forecast["date"]} 最{forecast["high"]} \
最{forecast["low"]} 白天天气: {forecast["day"]["type"]} 夜间天气: {forecast["night"]["type"]}
"""
    msg += """tips:
"""
    for tip in data["zhishus"]["zhishu"]:
        if tip["name"] in {"穿衣指数", "紫外线强度", "感冒指数", "污染指数", "舒适度"}:
            msg += f"""{tip["name"]}: {tip["detail"]}
"""

    print(msg)

if __name__ == '__main__':
    weather_msg_format(query_weather(query_city_code("嘉兴")))
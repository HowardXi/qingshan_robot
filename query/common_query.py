#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Xi WenHao
# @Email    : xiwenhao1994@gmail.com
# @Project  : qingshan
# @Time     : 2021/10/25 11:09
# @File     : common_query.py

from requests import get, post
from match.pets import query_pet_place, query_pet_cd, query_recored_pet
from urllib.request import quote
from query import jx3api_app, pet_api
import json
import time

# headers = {
#  'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
# }

def query_support_pet():
    pets = query_recored_pet()
    msg = ""
    index = 0
    for pet in pets:
        msg += "%s " % pet
        index += 1
        if index % 5 == 0:
            msg += "\n"
    return msg


def query_pet(server, pet=None, role=None):
    if not server or server == "全部":
        return """需要指明服务器, 使用方式是'蹲宠 {服务器名} {宠物名}', 宠物名可以写'全部'"""

    if role in (None,"全部"):
        role = ""
    if pet in (None,"全部"):
        pet = ""
    pet_cd = query_pet_cd(pet)
    if "小时" not in pet_cd:
        url = pet_api.format(
            server_name=server,
            pet_name=pet,
            role_name=role
        )
        req = get(url)
        res = req.json()
    else:
        msg = f"""蹲宠查询结果
服务器:{server}  """
        if pet:
            msg += f"""宠物:{pet}  地点:{query_pet_place(pet)}  cd:{pet_cd}"""
        return msg

    if req.status_code == 200 and res["code"] == 0:
        msg = f"""蹲宠查询结果
服务器:{server}  """
        if pet:
            msg += f"""宠物:{pet}  地点:{query_pet_place(pet)}  cd:{pet_cd}"""
        msg += "\n"
        for record in res["data"]["data"]:
            msg += f"""时间: {record["date_str"]}\n"""
        return msg
    else:
        return "查询出错 联系青山问一下"


def query_macro(xinfa):
    endpoint = "/macro"
    request = get(jx3api_app + endpoint, data=json.dumps({"name": xinfa}))
    if request.status_code == 200:
        data = request.json()["data"]
        return "奇穴方案: " + data["qixue"] + "\r\n宏:\r\n" + data["macro"]
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
    print(query_support_pet())

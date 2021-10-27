#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Xi WenHao
# @Email    : xiwenhao1994@gmail.com
# @Project  : qingshan
# @Time     : 2021/10/25 11:09
# @File     : common_query.py

from requests import get, post
from match.pets import query_pet_place, query_pet_cd, query_recored_pet, is_support_pet
from urllib.request import quote
from query import jx3api_app, pet_api
import json
import time

# headers = {
#  'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
# }

def format_support_pet():
    pets = query_recored_pet()
    msg = ""
    index = 0
    for pet in pets:
        msg += "%s " % pet
        index += 1
        if index % 5 == 0:
            msg += "\n"
    return msg


def query_personal_pet_records(server, role_name):
    url = pet_api.format(
        server_name=server,
        pet_name=",".join(query_recored_pet()),
        role_name=role_name
    )
    msg = f"""蹲宠查询结果\n服务器:{server}  角色: {role_name}"""
    req = get(url)
    res = req.json()
    datetime_normal = True
    if req.status_code == 200 and res["code"] == 0:
        msg += "\n"
        if res["data"]["data"]:
            for record in res["data"]["data"]:
                msg += f"""宠物: {record["serendipity"]}"""
                if record["date_str"]:
                    msg += """时间: {record["date_str"]}\n"""
                else:
                    datetime_normal = False
                    msg += "\n"
            if not datetime_normal:
                msg += "查询不到时间呢, 我是辣鸡, 哭惹\n"
        else:
            msg += "没有查询到记录"
    return msg

def query_server_pet(server, pet=None):
    if not server or server == "全部":
        return """需要指明服务器, 使用方式是'蹲宠 {服务器名} {宠物名}', 宠物名可以写'全部'来查询所有宠物"""
    pet_cd = query_pet_cd(pet)

    if pet in (None, "全部"):
        # 避免 '全部' 关键字查询出错
        pet_cd = "小时"
    else:
        if not is_support_pet(pet):
            return "查不到这个宠物的信息, 看看是不是在支持列表里吧"
    msg = f"""蹲宠查询结果\n服务器:{server}  """
    if pet:
        msg += f"""宠物:{pet}  地点:{query_pet_place(pet)}  cd:{pet_cd}"""

    if "小时" in pet_cd:
        url = pet_api.format(
            server_name=server,
            pet_name=pet.replace("全部", ",".join(query_recored_pet())),
            role_name=""
        )
        req = get(url)
        res = req.json()
    else:
        if pet:
            msg += f"""{pet}的下一个有缘人就是你 快去摸!"""
        return msg
    if req.status_code == 200 and res["code"] == 0:
        msg += "\n"
        if res["data"]["data"]:
            for record in res["data"]["data"]:
                msg += f"""宠物: {record["serendipity"]} 时间: {record["date_str"]}\n"""

        else:
            msg += "没有查询到记录"
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
    # print(query_server_pet("天鹅坪", "果果"))
    print(query_personal_pet_records("天鹅坪", "与晋长安"))
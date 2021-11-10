#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Xi WenHao
# @Email    : xiwenhao1994@gmail.com
# @Project  : qingshan
# @Time     : 2021/10/25 14:50
# @File     : server.py
import json
from subprocess import getoutput

import websocket
from loguru import logger

from exception import QsBaseException
from for_fun.random_meme import draw_a_meme
from gocqhttp.action.parse_msg import cqcode_num, parse_cqcode
from gocqhttp.action.send_msg import send_group_msg, image_cq_wrapper, \
    text2image
from match.server_alias import alias2server
from match.xinfa import xinfa_set, match_xinfa
from music.music_api import query_song_id
from query.common_query import query_macro, query_heighten, query_daily, \
    query_gold_price, format_support_pet, query_server_pet, \
    query_personal_pet_records, query_price, query_server_state
from query.static import query_saohua, flatterer_diary, daily_material
from settings import cfg, gocq_cfg
from text2image.txt2img import FlatererDiary, remove_file
from query.weather import weather_msg_format, query_weather, query_city_code

@logger.catch
def on_message(ws, message):
    msg = json.loads(message)
    # logger.info(f"recv msg: {msg}")
    if "message_type" not in msg or msg["message_type"] not in ("group",):
        return

    if "[CQ" in msg["message"]:
        for cq in msg["message"].split(" "):
            cq_obj = parse_cqcode(cq)
            logger.info(
                f"recv msg={msg['message']}, parse cqcode result={cq_obj}")
            if cq_obj["type"] == "at" and \
                    cq_obj["args"]["qq"] == gocq_cfg["account"]["uin"]:
                path = draw_a_meme()
                send_group_msg(msg["group_id"], image_cq_wrapper(path))
                remove_file(path)
                return
        return
    op = msg["message"].split(" ")[0]
    args = msg["message"].split(" ")[1:] or [None, ]
    logger.info(f"split message: op={op}, args={args}")

    if op == "帮助":
        send_group_msg(msg["group_id"], image_cq_wrapper(text2image(helper())))
        return
    if op == "宏":
        # @ 宏, 可以查询这个心法的宏 食用方法:'宏 {心法}'
        logger.info(f"query macro op=宏, args={args}")
        if args[-1] in xinfa_set:
            result = query_macro(match_xinfa(args[-1]))
            send_group_msg(msg["group_id"], result)
        else:
            send_group_msg(msg["group_id"], "找不到这个心法的宏呢")
        return
    if op == "小药":
        # @ 小药, 查询当前版本小药
        image_ref = query_heighten(match_xinfa("冰心"))
        send_group_msg(msg["group_id"],
                       f"[CQ:image,file={image_ref},id=40000]")
        return
        # if op == "来张图":
    #     # TODO 图片要缓存到本地?
    #     image_ref = random_image()
    #     send_group_msg(msg["group_id"],
    #                    f"[CQ:image,image={image_ref},id=40000]")

    if op == "来句骚话":
        # @ 来句骚话, 骚好友骚世界骚门派必备
        send_group_msg(msg["group_id"], query_saohua())
        return
    if op == "日常":
        # @ 日常, 查询今天的日常
        send_group_msg(msg["group_id"], query_daily(args[-1]))
        return
    if op == "金价":
        # @ 金价, 查询这会儿的金价(半小时更新)
        send_group_msg(msg["group_id"], query_gold_price(args[-1]))
        return
    if op == "当前bot版本":
        # if sender in super_admins
        send_group_msg(msg["group_id"], getoutput("git rev-parse HEAD"))
        return
    if op == "点歌":
        # @ 点歌, 给大家分享一首歌, 食用方法: '点歌 {歌名}'
        result = query_song_id(args[-1])
        send_group_msg(msg["group_id"], f"[CQ:music,type=qq,id={result}]")
        return
    if op == "财富密码":
        # @ 财富密码, 查询今天的蚊子腿福利
        send_group_msg(msg["group_id"], daily_material())
        return
    if op == "查询蹲宠":
        # @ 查询蹲宠, 查询现在支持的蹲宠
        send_group_msg(msg["group_id"], format_support_pet())
        return
    if op == "蹲宠":
        # @ 蹲宠, 查询全服最近对应宠物的触发时间 食用方法:'蹲宠 {服务器} {宠物名}' 其中宠物名可以写"全部"
        server, pet = args
        server = alias2server(server)
        send_group_msg(msg["group_id"],
                       query_server_pet(server=server, pet=pet))
        return
    if op == "查询角色宠物":
        # @ 查询角色宠物, 查询指定角色名的最近宠物触发情况 食用方法:'查询角色宠物 {服务器} {角色名}' 有时候会获取不到具体时间
        server, role = args
        server = alias2server(server)
        send_group_msg(msg["group_id"],
                       query_personal_pet_records(server=server,
                                                  role_name=role))
        return
    if op == "物价查询":
        # @ 物价查询, 查询指定服务器最近指定物品的交易情况, 食用方法: '物价查询 {服务器} {物品名}' 服务器写别名也行
        server = "全部"
        server = alias2server(server)
        if len(args) == 2:
            server, item = args
        elif len(args) == 1:
            item = args[0]
        else:
            send_group_msg(msg["group_id"], "查询命令不正确")

        path = text2image(query_price(server, item))
        send_group_msg(msg["group_id"], image_cq_wrapper(path))
        remove_file(path)
        return
    if op == "开服":
        # @ 开服, 查询服务器开服状态, 食用方法: '开服 {服务器}'
        server = args[-1]
        server = alias2server(server)
        send_group_msg(msg["group_id"], query_server_state(server))
        return

    # if  op == "沙盘":
    #     # @ 沙盘, 查询指定服务器沙盘状态, 使用: '沙盘 {服务器}'
    #     server = args[-1]
    #     server = alias2server(server)
    #     image_ref = query_server_sandbox(server)
    #     send_group_msg(msg["group_id"], f"[CQ:image,url={image_ref},
    #     id=40000]")

    if op == "舔狗日记":
        # @ 舔狗日记, 谁会拒绝一个深情舔狗的语录呢
        content = flatterer_diary()
        img = FlatererDiary(content)
        path = img.create()
        send_group_msg(msg["group_id"], image_cq_wrapper(path))
        remove_file(path)
        return

    if op == "来张图":
        # @ 来张图, 返回一个随机的沙雕表情包
        path = draw_a_meme()
        send_group_msg(msg["group_id"], image_cq_wrapper(path))
        remove_file(path)
        return

    if op == "天气":
        # @ 天气, 查询天气, 比如'天气 西城'
        if not args:
            return
        try:
            text = weather_msg_format(query_weather(query_city_code(args[0])))
            logger.info("query weather %s" % text)
            path = text2image(text)
            send_group_msg(msg["group_id"], image_cq_wrapper(path))
            remove_file(path)
        except QsBaseException as e:
            send_group_msg(msg["group_id"], str(e))

        return

def on_error(ws, error):
    logger.error(error)
    if isinstance(error, QsBaseException):
        send_group_msg(error.group_id, str(error))
        logger.info("回复错误处理消息%s to %s" % (str(error), error.group_id))


def on_close(ws):
    logger.warning("websocket closed.")


def helper():
    with open("gocqhttp/server.py", "r", encoding="utf-8") as f:
        lines = f.readlines()
    help_text = ["帮助文档:"]
    for line in lines:
        line = line.strip()
        if line.startswith("# @ "):
            line = line.replace("# @ ", "")
            keyword, desc = line.split(",", maxsplit=1)
            keyword = "关键字: '%s'" % keyword
            desc = "说明:" + desc
            help_text.append("%s    %s" % (keyword.ljust(20), desc.ljust(20)))
    return "\r\n".join(help_text)


ws = websocket.WebSocketApp(
    cfg["gocqhttp"]["ws_addr"],
    on_message=on_message,
    on_error=on_error,
    on_close=on_close)

if __name__ == '__main__':
    print(helper())

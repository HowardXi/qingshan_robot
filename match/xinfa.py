#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Xi WenHao
# @Email    : xiwenhao1994@gmail.com
# @Project  : qingshan
# @Time     : 2021/10/25 15:51
# @File     : xinfa.py

xinfa = {
    "冰心": "冰心诀",
    "分山": "分山劲",
    "花间": "花间游",
    "离经": "离经易道",
    "铁骨": "铁骨衣",
    "焚影": "焚影圣诀",
}

xinfa_set = set(xinfa.keys())

def match_xinfa(abbr:str) -> str:
    """
    :param abbr: 心法缩写
    :return: 心法全称
    """
    return xinfa[abbr]
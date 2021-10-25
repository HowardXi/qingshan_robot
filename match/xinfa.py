#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Xi WenHao
# @Email    : xiwenhao1994@gmail.com
# @Project  : qingshan
# @Time     : 2021/10/25 15:51
# @File     : xinfa.py

xinfa = {
    "冰心": "冰心诀",
    "云裳": "云裳心经",
    "花间": "花间游",
    "离经": "离经易道",
    "毒经": "毒经",
    "补天": "补天诀",
    "莫问": "莫问",
    "相知": "相知",
    "无方": "无方",
    "灵素": "灵素",
    "傲血": "傲血战意",
    "铁牢": "铁牢律",
    "易筋": "易筋经",
    "洗髓": "洗髓经",
    "焚影": "焚影圣诀",
    "明尊": "明尊琉璃体",
    "分山": "分山劲",
    "铁骨": "铁骨衣",
    "紫霞": "紫霞功",
    "太虚": "太虚剑意",
    "天罗": "天罗诡道",
    "惊羽": "惊羽诀",
    "问水": "问水诀",
    "山居": "山居剑意",
    "笑尘": "笑尘诀",
    "北傲": "北傲诀",
    "凌海": "凌海诀",
    "隐龙": "隐龙诀",
    "太玄": "太玄经",
    "藏剑": "问水诀"
}

xinfa_set = set(xinfa.keys())

def match_xinfa(abbr:str) -> str:
    """
    :param abbr: 心法缩写
    :return: 心法全称
    """
    return xinfa[abbr]


if __name__ == '__main__':
    print(match_xinfa("冰心"))
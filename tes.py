#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Xi WenHao
# @Email    : xiwenhao1994@gmail.com
# @Project  : qingshan
# @Time     : 2021/11/8 16:11
# @File     : tes.py
from match.server_alias import alias2server
from gocqhttp.action.send_msg import image_cq_wrapper, text2image
from text2image.txt2img import Text2Img
from query.common_query import query_price

# print(query_server_pet("天鹅坪", "果果"))
# print(query_personal_pet_records("天鹅坪", "与晋长安"))
# text = query_price("天鹅坪", "五七")
print(image_cq_wrapper(text2image("你说你想买AJ，今天我去了叔叔的口罩厂做了一天的打包。拿到了两百块钱，"
        "加上我这几天省下的钱刚好能给你买一个鞋盒。即没有给我自己剩下一分钱，"
        "但你不用担心，因为厂里包吃包住。对了打包的时候，满脑子都是你，"
        "想着你哪天突然就接受我的橄榄枝了呢。而且今天我很棒呢，主管表扬我很能干，"
        "其实也有你的功劳啦，是你给了我无穷的力量。今天我比昨天多想你一点，比明天少想你一点。")))
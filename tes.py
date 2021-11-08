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
text = query_price("天鹅坪", "青盒子")
print(image_cq_wrapper(text2image(text)))
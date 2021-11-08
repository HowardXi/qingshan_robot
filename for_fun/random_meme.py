#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Xi WenHao
# @Email    : xiwenhao1994@gmail.com
# @Project  : qingshan
# @Time     : 2021/11/8 17:28
# @File     : random_meme.py
import imghdr

from requests import get
from random import randint, choice
from uuid import uuid4
from os.path import abspath
from query.utils import get_headers

API = "http://doutu.ucode.top/api/getpng?tokenId=F96C2856-02FA-4763-B82F-62D0E22AEE47&pageIndex=%s&pageSize=10"


def random_meme():
    random_page = randint(1, 400)  # 总共大概400页表情
    refs_req = get(url=API % random_page, headers=get_headers(), verify=False)
    image_ref = choice(refs_req.json()["Data"])["url"]
    return image_ref


def download(image_ref):
    content = get(image_ref, stream=True).content
    suffix = imghdr.what(None, content)
    file_path = "image_cache/%s.%s" % (uuid4().hex, suffix)
    with open(file_path, "wb+") as f:
        f.write(content)
    return abspath(file_path)


def draw_a_meme():
    path = download(random_meme())
    return path

if __name__ == '__main__':
    print(draw_a_meme())
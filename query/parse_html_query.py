#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Xi WenHao
# @Email    : xiwenhao1994@gmail.com
# @Project  : qingshan
# @Time     : 2021/10/29 17:45
# @File     : parse_html_query.py

from requests import get
from lxml.etree import HTML
from query.utils import get_headers


def query_all_sandbox():
    res = get("https://www.j3sp.com/", headers=get_headers())
    html = res.content
    e = HTML(html)
    servers = e.xpath('//*[@id="table"]/tbody/tr/td[7]/img//@alt')
    refs = e.xpath('//*[@id="table"]/tbody/tr/td[7]/img//@b0111ff7')

    sandbox = {}

    for server, ref in zip(servers, refs):
        server = server.split("- ")[-1]
        sandbox[server] = "https://img.j3sp.com/uploads/%s.png_small" % ref

    return sandbox
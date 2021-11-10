#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Xi WenHao
# @Email    : xiwenhao1994@gmail.com
# @Project  : qingshan
# @Time     : 2021/10/28 16:32
# @File     : database.py

from db.module import *
from sqlalchemy.orm import sessionmaker
session = sessionmaker(engine)()

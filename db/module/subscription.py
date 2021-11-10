#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Xi WenHao
# @Email    : xiwenhao1994@gmail.com
# @Project  : qingshan
# @Time     : 2021/11/8 18:18
# @File     : subscription.py

from sqlalchemy import Column, Integer, String, Boolean, BigInteger

from db.module import BaseModel

class Subscription(BaseModel):
    __tablename__ = 'subscription'
    id = Column(Integer, primary_key=True, autoincrement=True)
    server = Column(String,nullable=False,)
    group_id = Column(BigInteger, nullable=False, index=True)

BaseModel.metadata.create_all()
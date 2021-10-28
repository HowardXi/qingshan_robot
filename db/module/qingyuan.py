#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Xi WenHao
# @Email    : xiwenhao1994@gmail.com
# @Project  : qingshan
# @Time     : 2021/10/28 16:16
# @File     : qingyuan.py

from sqlalchemy import Column, Integer, String, Boolean, BigInteger

from db.module import BaseModel


class QingYuan(BaseModel):
    __tablename__ = 'qingyuans'
    id = Column(Integer, primary_key=True, autoincrement=True)
    server = Column(String)
    somatotype = Column(String, nullable=False)  # 门派体型
    yao = Column(Boolean, nullable=False)  # 妖号?
    camps = Column(String, nullable=False) # 阵营
    qq_id = Column(BigInteger, nullable=False, index=True)
    desc = Column(String)

BaseModel.metadata.create_all()

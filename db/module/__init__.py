#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Xi WenHao
# @Email    : xiwenhao1994@gmail.com
# @Project  : qingshan
# @Time     : 2021/10/28 16:15
# @File     : __init__.py.py

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer

engine = create_engine("sqlite:///db/qsbot.db")
Base = declarative_base(engine)


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


Base.metadata.create_all()
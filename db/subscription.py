#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Xi WenHao
# @Email    : xiwenhao1994@gmail.com
# @Project  : qingshan
# @Time     : 2021/11/8 18:55
# @File     : subscription.py
# 给开服提醒使用, 每个群可以订阅多个服务器, 需要检查权限

from loguru import logger

from db.module.subscription import Subscription


def add(session, server: str, group_id: int):
    new_sub = Subscription(
        server=server,
        group_id=group_id
    )
    logger.info("add new_sub record id %s, content %s" % (
        new_sub.id, str(new_sub)))
    session.add(new_sub)
    session.commit()
    logger.info("add new_sub record id %s ok" % new_sub.id)


def query_group_by_server(session, server: str):
    records = session.query(Subscription).filter_by(
        server=server).all()
    return [r.group_id for r in records]


def delete(session, server: str, group_id: int):
    records = session.query(Subscription).filter_by(
        group_id=group_id, server=server).all()
    for record in records:
        record.delete()
    session.commit()

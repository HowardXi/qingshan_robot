#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Xi WenHao
# @Email    : xiwenhao1994@gmail.com
# @Project  : qingshan
# @Time     : 2021/10/28 16:29
# @File     : qingyuan.py

from loguru import logger

from module.qingyuan import QingYuan


def add(session, server, somatotype, yao: bool, camps:str, desc, qq_id: int):
    '''
    :param session: db会话
    :param server: 服务器名
    :param somatotype: 门派体型
    :param yao: 妖号
    :param camps: 阵营
    :param qq_id: qq号
    :param desc: 简单描述自己
    :return: None
    '''
    new_find_qy = QingYuan(
        server=server,
        somatotype=somatotype,
        yao=yao,
        camps=camps,
        qq_id=qq_id,
        desc=desc
    )
    logger.info("add new find qy record id %s, content %s" % (
        new_find_qy.id, str(new_find_qy)))
    session.add(new_find_qy)
    session.commit()
    logger.info("add new find qy record id %s ok" % new_find_qy.id)


def query_all(session, server=None, somatotype=None, camps=None, yao=False):
    filters = []
    if server: filters.append(QingYuan.server == server)
    if somatotype: filters.append(QingYuan.somatotype == somatotype)
    if yao: filters.append(QingYuan.yao == yao)
    if yao: filters.append(QingYuan.camps == camps)
    candidates = session.query(QingYuan).filter(*filters).all()
    return candidates


def query_one(session, server=None, somatotype=None, camps=None, yao=False):
    filters = []
    if server: filters.append(QingYuan.server == server)
    if somatotype: filters.append(QingYuan.somatotype == somatotype)
    if yao: filters.append(QingYuan.yao == yao)
    if yao: filters.append(QingYuan.camps == camps)
    candidate = session.query(QingYuan).filter(*filters).first()
    return candidate


def delete(session, qq_id: int):
    records = session.query(QingYuan).filter_by(
        qq_id=qq_id).all()
    for record in records:
        record.delete()
    session.commit()

if __name__ == '__main__':
    from db.database import session
    add(session, "天鹅坪", "炮哥", False, "浩气", "随便来", 12345678901)
    print(query_one(session, "天鹅坪", "炮哥").to_dict())
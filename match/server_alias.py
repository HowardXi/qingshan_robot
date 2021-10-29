#!/usr/bin/env python
# -*- coding: utf-8 -*-

from exception import ServerNotFound

alias_server_mapping = {
    "全部": "全部",
    "天鹅坪": "纵月",
    "唯我独尊": "唯满侠",
}
server_alias_mapping = {v: k for v, k in alias_server_mapping.items()}

def alias2server(alias):
    if alias in alias_server_mapping:
        return alias_server_mapping[alias]
    else:
        return None

def server2alias(server_alias):
    """
    :param server_alias: 服务器俗名
    :return: 主服务器名
    """
    if server_alias in server_alias_mapping:
        return server_alias_mapping[server_alias]
    if server_alias in alias_server_mapping:
        return server_alias
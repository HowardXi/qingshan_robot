#!/usr/bin/env python
# -*- coding: utf-8 -*-

from exception import ServerNotFound

alias_server_mapping = {
    "全部": "全部",
    "纵月": "天鹅坪",
    "唯满侠": "唯我独尊",
    "双梦": "梦江南",

}
server_alias_mapping = {v: k for k, v in alias_server_mapping.items()}

def alias2server(server_alias):
    """
    :param server_alias: 服务器俗名
    :return: 主服务器名
    """
    if server_alias in alias_server_mapping:
        return alias_server_mapping[server_alias]
    if server_alias in server_alias_mapping:
        return server_alias


def server2alias(server):
    return server_alias_mapping[server]


if __name__ == '__main__':
    print(server2alias("天鹅坪"))
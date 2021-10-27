#!/usr/bin/env python
# -*- coding: utf-8 -*-


alias_server_mapping = {
    "天鹅坪": "纵月",
    "唯我独尊": "唯满侠",
}
server_alias_mapping = {v: k for v, k in alias_server_mapping.items()}

def alias2server(alias):
    if alias in alias_server_mapping:
        return alias_server_mapping[alias]
    else:
        return None

def server2alias(server_name):
    if server_name in server_alias_mapping:
        return server_alias_mapping[server_name]
    else:
        return None

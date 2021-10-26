#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Xi WenHao
# @Email    : xiwenhao1994@gmail.com
# @Project  : qingshan
# @Time     : 2021/10/19 18:25
# @File     : settings.py

from loguru import logger
from toml import load

log = logger


def load_settings(path="./settings.toml"):
    cfg = None
    with open(path, "r") as f:
        cfg = load(f)
    if not cfg:
        log.error("can not find settings file")
    log.info("load settings done")
    for opt, value in cfg.items():
        log.info(f"cfg: {opt} = {value}")
    return cfg


cfg = load_settings()
if cfg["base"]["debug"]:
    logger.add(sink="logs/demo.logs", level="DEBUG")
else:
    log.add(sink="logs/demo.logs", level="WARNING")

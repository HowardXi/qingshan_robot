#!/usr/bin/env python
# -*- coding: utf-8 -*-

from json import load

with open("../db/pets.json", "r", encoding="utf-8") as f:
    pet_data = load(f)

def query_pet_cd(name):
    if name in pet_data:
        return pet_data[name]["cd"]
    else:
        return "没有cd"

def query_pet_place(name):
    if name in pet_data:
        return pet_data[name]["place"]
    else:
        return "空"

def query_recored_pet():
    return pet_data.keys()
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from json import load
import os

pet_file = "db/pets.json"
if not os.path.exists(pet_file):
    pet_file = "../db/pets.json"

with open(pet_file, "r", encoding="utf-8") as f:
    pet_data = load(f)

def is_support_pet(name):
    return name in pet_data

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
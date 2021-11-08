#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Xi WenHao
# @Email    : xiwenhao1994@gmail.com
# @Project  : qingshan
# @Time     : 2021/11/8 10:07
# @File     : txt2img.py

import time
from random import choice
from uuid import uuid4
from os.path import abspath
from loguru import logger

from PIL import Image, ImageDraw, ImageFont


class Text2Img(object):
    def __init__(self, text):
        logger.info("convert text to image, text: %s" % text)
        self.text = text
        self.font_size = 14
        self.width = 250
        self.font = ImageFont.truetype("text2image/zhangqiling.ttf", self.font_size)
        self.hangju = self.font_size + 5
        self.splited = self.split_text()

    def split_text(self):
        lines = []
        line = ""
        line_width = 0
        char_num = 0  # 被处理了的char 用来处理最后一行不到宽度无法加入被分割text的问题
        for char in self.text:
            line += char
            line_width += self.font.getsize(char)[0]
            if line_width >= (self.width - self.font_size) or char == "\n":
                char_num += len(line)
                lines.append("".join(line))
                line = ""
                line_width = 0
        lines.append(self.text[char_num: -1])
        return lines, len(lines)

    def draw_text(self):
        diary_img = Image.new("RGB", (self.width, self.hangju * self.splited[1]),
                              (255, 255, 255))
        draw = ImageDraw.Draw(diary_img)
        # 左上角开始
        x, y = 0, 0
        lines, lens = self.splited
        for line in lines:
            draw.text((x, y), line, fill=(0, 0, 0), font=self.font)
            y += self.hangju
        file_path = "image_cache/%s.png" % uuid4().hex
        diary_img.save(file_path)
        return file_path


class FlatererDiary(object):
    def __init__(self, text):
        self.weather = choice(
            ["阴", "晴", "小雨", "大雨", "暴雨", "雾霾", "很晒", "大雪", "暴雪", "寒冷", "多云"])
        # 文本
        self.today = time.strftime('%m月%d日', time.localtime())
        self.text = "%s %s                                         " % (
            self.today, self.weather) + text
        self.diary_width = 250
        self.font_size = 14
        self.font = ImageFont.truetype("text2image/msyh.ttf", self.font_size)
        self.hangju = self.font_size + 5
        self.header_path = "text2image/tiangou.png"
        self.header = Image.open(self.header_path)
        self.splited = self.split_text()

    def computed_daily_height(self, total_lines):
        text_height = self.hangju * total_lines
        total_height = self.header.size[-1] + text_height
        return total_height

    def split_text(self):
        lines = []
        line = ""
        line_width = 0
        char_num = 0  # 被处理了的char 用来处理最后一行不到宽度无法加入被分割text的问题
        for char in self.text:
            line += char
            line_width += self.font.getsize(char)[0]
            if line_width >= (self.diary_width - self.font_size):
                char_num += len(line)
                lines.append("".join(line))
                line = ""
                line_width = 0
        lines.append(self.text[char_num: -1])
        return lines, len(lines)

    def draw_text(self, height):
        diary_img = Image.new("RGB", (self.diary_width, height),
                              (255, 255, 255))
        draw = ImageDraw.Draw(diary_img)
        # 左上角开始
        x, y = 0, 0
        lines, lens = self.splited
        for line in lines:
            draw.text((x, y), line, fill=(0, 0, 0), font=self.font)
            y += self.hangju
        # diary_img.save("re.png")
        return diary_img

    def create(self):

        total_height = self.computed_daily_height(self.splited[1])
        bg = Image.new('RGB', (self.diary_width, total_height), )
        bg.paste(self.header, (0, 0))
        diary_content = self.draw_text(
            total_height - self.header.size[1] + 100)
        bg.paste(diary_content, (0, self.header.size[1]))
        file_path = "image_cache/%s.png" % uuid4().hex
        bg.save(file_path)
        return abspath(file_path)


if __name__ == '__main__':
    n = Text2Img(
        "你说你想买AJ，今天我去了叔叔的口罩厂做了一天的打包。拿到了两百块钱，"
        "加上我这几天省下的钱刚好能给你买一个鞋盒。即没有给我自己剩下一分钱，"
        "但你不用担心，因为厂里包吃包住。对了打包的时候，满脑子都是你，"
        "想着你哪天突然就接受我的橄榄枝了呢。而且今天我很棒呢，主管表扬我很能干，"
        "其实也有你的功劳啦，是你给了我无穷的力量。今天我比昨天多想你一点，比明天少想你一点。")
    print(n.draw_text())

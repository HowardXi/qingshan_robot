#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Xi WenHao
# @Email    : xiwenhao1994@gmail.com
# @Project  : qingshan
# @Time     : 2021/10/26 17:17
# @File     : music_api.py

from QQMusicAPI import QQMusic

class MusicAPI(object):
    def __init__(self, song_name):
        self.music_list = QQMusic.search(song_name)
        self._song = self.music_list.data[0]
        self.mid = self._song.song_mid



if __name__ == '__main__':
    song = MusicAPI("好运来")
    print(song.mid)
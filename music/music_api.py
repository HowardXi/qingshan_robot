#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Xi WenHao
# @Email    : xiwenhao1994@gmail.com
# @Project  : qingshan
# @Time     : 2021/10/26 17:17
# @File     : music_api.py

from music.QQMusicAPI import QQMusic

class MusicAPI(object):
    def __init__(self, song_name):
        self.music_list = QQMusic.search(song_name)
        self._song = self.music_list.data[0]
        self.mid = self._song.song_mid
        self.id = self._song.song_id

def query_song_id(song_name):
    return QQMusic.search(song_name).data[0].song_id

if __name__ == '__main__':
    print(query_song_id("好运来"))
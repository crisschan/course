#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 10:07 上午
# @Author  : CrissChan
# @Site    : https://blog.csdn.net/crisschan
# @File    : main主要用来生成音频、视频等的入口
from page_one import PageOne

if __name__ == '__main__':
    pgo = PageOne(txt_root='./txt/', txt_file='clover',
                 wav_root='./wav/', img_root='./img/',
                  img_file='1.JPG',class_video_root='./onevideo/')
    pgo.get_one()






#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 10:07 上午
# @Author  : CrissChan
# @Site    : https://blog.csdn.net/crisschan
# @File    : main主要用来生成音频、视频等的入口
from page_one import PageOne
from class_video import ClassVideo
from setting import *
from remover import Remover
import os
if __name__ == '__main__':

    Remover.dir_under('./tmp')
    try:
        os.mkdir(ONEVIDEO_ROOT)
    except:
        print(ONEVIDEO_ROOT+'已经存在')
    try:
        os.mkdir(WAV_ROOT)
    except:
        print(WAV_ROOT + '已经存在')
    try:
        os.mkdir(TMP_ROOT)
    except:
        print(TMP_ROOT + '已经存在')
    try:
        os.mkdir(ONEVIDEO_ROOT)
    except:
        print(ONEVIDEO_ROOT + '已经存在')
    try:
        os.mkdir(TMP_ROOT)
    except:
        print(TMP_ROOT + '已经存在')
    try:
        os.mkdir(CLASSVIDEO_ROOT)
    except:
        print(CLASSVIDEO_ROOT + '已经存在')

    istep=1
    while istep<=11:
        pgo = PageOne(txt_root=TXT_ROOT, txt_file=str(istep),
                      wav_root=WAV_ROOT, img_root=IMG_ROOT,
                      img_file=str(istep)+'.png', class_video_root=ONEVIDEO_ROOT)
        pgo.get_one()
        istep=istep+1
    cv = ClassVideo(ONEVIDEO_ROOT)
    cv.get_class(CLASSVIDEO_ROOT,'class1.mp4')


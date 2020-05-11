#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 10:07 上午
# @Author  : CrissChan
# @Site    : https://blog.csdn.net/crisschan
# @File    : main主要用来生成音频、视频等的入口
from page_one import PageOne
from class_video import ClassVideo
from setting import *

if __name__ == '__main__':


    istep=1
    while istep<=13:
        pgo = PageOne(txt_root=TXT_ROOT, txt_file=str(istep),
                      wav_root=WAV_ROOT, img_root=IMG_ROOT,
                      img_file=str(istep)+'.jpg', class_video_root=ONEVIDEO_ROOT)
        pgo.get_one()
        istep=istep+1
    cv = ClassVideo(ONEVIDEO_ROOT)
    cv.get_class(CLASSVIDEO_ROOT,'class1.mp4')


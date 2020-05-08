#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 10:07 上午
# @Author  : CrissChan
# @Site    : https://blog.csdn.net/crisschan
# @File    : main主要用来生成音频、视频等的入口
from page_one import PageOne
from class_video import ClassVideo

if __name__ == '__main__':


    istep=1
    while istep<=2:
        pgo = PageOne(txt_root='./txt/', txt_file=str(istep),
                      wav_root='./wav/', img_root='./img/',
                      img_file=str(istep)+'.JPG', class_video_root='./onevideo/')
        pgo.get_one()
        istep=istep+1
    cv = ClassVideo('./onevideo/')
    cv.get_class('./class_video/','class1.mp4')

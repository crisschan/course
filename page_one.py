#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 10:24 上午
# @Author  : CrissChan
# @Site    : https://blog.csdn.net/crisschan
# @File    : page_one.py

from booklet_wav import BookletWav
from img2video import Img2Video
from audio4video import Audio4Video
import librosa
from setting import *
import os
class PageOne(object):
    def __init__(self, txt_root='./txt/', txt_file='clover',
                 wav_root='./wav/', img_root='./img/', img_file='',class_video_root='./onevideo/'):
        '''

        :param txt_root: 文本文件存储位置
        :param txt_file: 文本文件名称
        :param wav_root: 生成音频文件位置
        '''
        self.txt_root = txt_root
        self.txt_file = txt_file
        self.wav_root = wav_root
        self.img_root=img_root
        self.img_file=img_file
        self.class_video_root=class_video_root

    def get_one(self):
        bl = BookletWav(self.txt_root, self.txt_file, target_dir=self.wav_root)
        # 生成音频mp3种
        self.mp3_root,self.mp3_file = bl.to_mp3()


        time_duration = librosa.get_duration(filename=self.mp3_root+self.mp3_file)

        i2v = Img2Video(self.img_root,img_file=self.img_file, video_root=TMP_ROOT, video_file=self.img_file+'.mp4', fps=1 / time_duration)
        i2v.to_video()
        a4v = Audio4Video(TMP_ROOT, self.img_file+'.mp4', self.mp3_root, self.mp3_file)
        ## 在合并多个视频的时候出现了1和10排序在一起，这可能是因为使用了sort()函数的时候排序是按照字符串顺序排序的，因此这里我想通过
        ## {:0>4d}.format(int(self.img_file))方式格式化onevideo文件名为0001这种格式
        ## 但是我觉得这里做个事约束对后续影响由点到，这一个想法暂时暂停，寻求在class_video里面解决sort问题
        a4v.combin( self.class_video_root, os.path.splitext(self.img_file)[0]+'.mp4')

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
        # 生成音频wav和mp3两种
        self.wav_root,self.wav_file = bl.to_wav()
        self.mp3_root,self.mp3_file = bl.to_mp3()

        time_duration = librosa.get_duration(filename=self.mp3_root+self.mp3_file)

        i2v = Img2Video(self.img_root,img_file=self.img_file, video_root='./tmp/', video_file=self.img_file+'.mp4', fps=1 / time_duration)
        i2v.to_video()
        a4v = Audio4Video('./tmp/', self.img_file+'.mp4', self.mp3_root, self.mp3_file)
        a4v.combin( self.class_video_root, self.img_file+'.mp4')

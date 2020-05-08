#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 1:47 下午
# @Author  : CrissChan
# @Site    : https://blog.csdn.net/crisschan
# @File    : merge_wav.py
# @intro   : 合并多个wav文件为一个

from pydub import AudioSegment

class MergeWav(object):
    def __init__(self,wav_dir,wav_list):
        '''
        合并音频
        :param wav_list: 全部音频文件列表
        '''
        self.wav_list  = wav_list
        self.wav_dir=wav_dir
        self.input_list = []
        self.inputdBFS_list = []
        self.time_list = []
        self.__get_music_proprity()
    def __get_music_proprity(self):
        self.output_dBFS=0
        for awav in self.wav_list:
            amusic = AudioSegment.from_wav(self.wav_dir+awav)
            self.input_list.append(amusic)
            self.inputdBFS_list.append(amusic.dBFS)
            self.time_list.append(len(amusic))
            self.output_dBFS = (self.output_dBFS*2+amusic.dBFS)/2

    def save_wav(self,output_file):
        '''

        :param output_file: 合并文件的全路径目录
        :return:
        '''
        output_music = self.input_list[0]
        istep = 1
        while istep<len(self.input_list):
            output_music=output_music+self.input_list[istep]
            istep=istep+1
        output_music.export(output_file, format="wav")





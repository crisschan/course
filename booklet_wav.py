#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 10:18 上午
# @Author  : CrissChan
# @Site    : https://blog.csdn.net/crisschan
# @File    : booklet_wav.py


from save_wav import SaveWav
import os
from merge_wav import MergeWav
from split_txt import SplitTxt
from pydub import AudioSegment


class BookletWav(object):
    '''
    通过输入音频稿文本生成音频文件
    '''

    def __init__(self, txt_dir, txt_file,target_dir='./wav/'):
        '''

        :param txt_dir:文本存储目录,结尾以/结束
        :param txt_file:文本名称
        :param target_dir:存储生成音频文件路径，生成文件和文本同名
        '''
        self.txt_file = txt_file
        self.txt_dir = txt_dir
        self.target_dir=target_dir

    def to_wav(self):
        '''
        生成和txt_file同名的wav文件，在wav下
        return:生成的wav文件的全路径
        '''

        if not os.path.exists(self.target_dir + self.txt_file):
            os.mkdir(self.target_dir + self.txt_file)

        target_dir = self.target_dir + self.txt_file + '/'
        # 注释默认按照line读取使用split算法
        # rf = open(self.txt_dir+self.txt_file, 'r')
        # line_list = rf.readlines()
        ############################
        ## split算法，全部文本每一个标点符号都会区分
        sTxt = SplitTxt(self.txt_dir, self.txt_file)
        line_list = sTxt.split_aline()
        ########################

        SaveWav(target_dir, line_list)
        wav_list = os.listdir(target_dir)
        wav_list.sort()
        mergwav = MergeWav(target_dir, wav_list)
        mergwav.save_wav(target_dir + self.txt_file + '.wav')
        self.__clear_temp(wav_list)

        return (target_dir , self.txt_file + '.wav')

    def to_mp3(self):
        '''
        和wav相同目录下生成mp3格式音频
        return 返回生成MP3文件的全路径
        '''

        if not os.path.exists(self.target_dir + self.txt_file + '.wav'):
            self.to_wav()
        if not os.path.exists(self.target_dir + self.txt_file):
            os.mkdir(self.target_dir + self.txt_file)
        target_dir = self.target_dir + self.txt_file + '/'
        AudioSegment.from_wav(target_dir + self.txt_file + '.wav').export(target_dir + self.txt_file + '.mp3',
                                                                          format='mp3')

        return (target_dir , self.txt_file + '.mp3')

    def __clear_temp(self, file_list):

        for afile in file_list:
            if os.path.exists(afile):
                os.remove(afile)




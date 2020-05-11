#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/4/28 11:11 下午
# @Author  : CrissChan
# @Site    : https://blog.csdn.net/crisschan
# @File    : save_wav.py
# @intro   : tx的tts返回的wav编码存储为wav音频文件
from tts_tx import TTS_TX
import base64
class SaveWav(object):
    '''
    从腾讯云的tts处理的音频base64编码转存wav文件，一行文字一个音频。
    '''
    def __init__(self,wav_dir,txt_list):
        '''

        :param wav_dir: 音频存储位置，以/结尾
        :param txt_list: 转音频文字列表
        '''
        self.wav_dir = wav_dir
        self.txt_list = txt_list
        self.__save()

    def __save(self):

        iseq = 0
        tts_tx = TTS_TX()
        for aline in self.txt_list:
            iseq=iseq+1
            aline = aline.replace('\n','')
            try:
                wav_txt = tts_tx.tts(aline)
                if(wav_txt!='error'):
                    file1 = open(self.wav_dir+str(iseq).zfill(5) + ".wav", "wb")  # 写入二进制文件
                    text = base64.b64decode(wav_txt)  # 进行解码
                    file1.write(text)
                    file1.close()  # 写入文件完成后需要关闭文件才能成功写入
            except:
                wav_txt = tts_tx.tts(aline)
                if (wav_txt != 'error'):
                    file1 = open(self.wav_dir + str(iseq).zfill(5) + ".wav", "wb")  # 写入二进制文件
                    text = base64.b64decode(wav_txt)  # 进行解码
                    file1.write(text)
                    file1.close()  # 写入文件完成后需要关闭文件才能成功写入



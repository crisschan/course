#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 1:03 上午
# @Author  : CrissChan
# @Site    : https://blog.csdn.net/crisschan
# @File    : audio_video.py
import librosa
import moviepy.editor as mpe

class Audio4Video(object):
    def __init__(self, video_root, video_file, audio_root, audio_file):
        '''

        :param video_root: 视频文件所在目录以/结尾
        :param video_file: 视频文件名字
        :param audio_root: 音频文件所在目录，以/结尾
        :param audio_file: 音频文件名称
        '''
        self.video_root = video_root
        self.video_file = video_file
        self.audio_root = audio_root
        self.audio_file = audio_file


    def __combine_audio(self, outvideo_root, outvideo_file):
        my_clip = mpe.VideoFileClip(self.video_root+self.video_file)
        audio_background = mpe.AudioFileClip(self.audio_root+self.audio_file)
        n_frames = my_clip.reader.nframes
        final_clip = my_clip.set_audio(audio_background)
        final_clip.write_videofile(outvideo_root+outvideo_file, fps=n_frames, audio_codec="aac")


    def combin(self, outvideo_root, outvideo_file):
        '''
        合成视频文件
        :param outvideo_root: 合成视频所在路径
        :param outvideo_file: 合成视频名称
        :return: null
        '''
        self.__combine_audio(outvideo_root,outvideo_file)
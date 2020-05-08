#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 9:31 上午
# @Author  : CrissChan
# @Site    : https://blog.csdn.net/crisschan
# @File    : img2video.py
import cv2
from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
import os


class Img2Video(object):
    def __init__(self, img_root, img_file='', video_root='./', video_file='c.mp4', fps=1):
        '''

        :param img_root: 图片存储的文件夹
        :param img_file: 图片文件名，如果输入了了图片名称，那么就会生成一个图片的视频
        :param video_root: 生成视频所在目录，默认是当前目录
        :param video_file: 生成视频文件的名字，默认是c.avi,扩展格式支持持mp4
        :param picper: 一张图片展示picper秒,正整形，默认为1，也就是1秒钟
        '''
        self.img_root = img_root

        self.video_root = video_root
        self.video_file = video_file
        self.img_file = img_file

        self.fps = fps

    def to_video(self):
        '''
        生成mp4视频文件
        :return:null
        '''
        size = (1920, 1080)
        fourcc = VideoWriter_fourcc(*"mp4v")  # 支持jpg
        videoWriter = cv2.VideoWriter(self.video_root + self.video_file, fourcc, self.fps, size)
        if len(self.img_file)==0:
            im_names = os.listdir(self.img_root)
            for im_name in im_names:
                frame = cv2.imread(self.img_root + im_name)
                frame = cv2.resize(frame, size)  # 注意这里resize大小要和视频的一样
                videoWriter.write(frame)
            videoWriter.release()
        else:
            im_name=self.img_file
            frame = cv2.imread(self.img_root + im_name)
            frame = cv2.resize(frame, size)  # 注意这里resize大小要和视频的一样
            videoWriter.write(frame)
            videoWriter.release()

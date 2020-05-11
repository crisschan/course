#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 1:45 下午
# @Author  : CrissChan
# @Site    : https://blog.csdn.net/crisschan
# @File    : class_video.py
from moviepy.editor import *
import os
from setting import *
class ClassVideo(object):

    def __init__(self,video_root):
        '''

        :param video_root: 生成的单个视频
        '''
        self.video_root=video_root
        self.video_list = []
        self.__get_files()

    def __get_files(self):

        # 访问 video 文件夹 (假设视频都放在这里面)
        for root, dirs, files in os.walk(self.video_root):
            # 按文件名排序
            files.sort()
            ## 加入iFile只是为了能够避免上面files.sort()是按照字符串排序的，这个字符串排序会将1.MP4和10.MP4
            ## 放到一起，我们认为约束了ppt就是1，2，3 那么我就直接在这里1，2，3这样的约束
            ifile = 1
            # 遍历所有文件

            for file in files:
                # 如果后缀名为 .mp4
                if os.path.splitext(file)[1] == '.mp4':
                    # 拼接成完整路径
                    filePath = os.path.join(root, str(ifile)+'.mp4')
                    ifile=ifile+1
                    # 载入视频
                    video = VideoFileClip(filePath)
                    # 添加到数组
                    self.video_list.append(video)
    def get_class(self,outclass_root,outclass_file):
        # 拼接视频
        final_clip = concatenate_videoclips(self.video_list)

        final_clip.to_videofile(outclass_root+outclass_file, remove_temp=True, audio_codec="aac")

if __name__ == '__main__':
    cv = ClassVideo(ONEVIDEO_ROOT)
    cv.get_class(CLASSVIDEO_ROOT, 'class1.mp4')
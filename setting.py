#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/5/9 3:56 下午
# @Author  : CrissChan
# @Site    : https://blog.csdn.net/crisschan
# @File    : setting.py
# 全部配置都在这里

## 文本目录，按照和图片同名并且按照1、2、3 的方式存储，无扩展名
TXT_ROOT = './origin/txt/'
## 图片目录，按照1，2，3方式存储，jpg扩展名，同ppt里的页的顺序编号
IMG_ROOT = './origin/img/'

## 一个ppt是一节课，那么合并一节课的视频，就是一个
CLASSVIDEO_ROOT = './classvideo/'
## 同txt文件的音频文件
WAV_ROOT = './tmp/wav/'
## 存放一些临时文件or过程中文件
TMP_ROOT = './tmp/tmp/'
## 生成的每一个图片+文本的音频的 小视频
ONEVIDEO_ROOT = './tmp/onevideo/'

## 腾讯云的tts的secretId, secretKey

SECRETID='AKIDXpslPnL7vlKeiYtXjvrX5QHsFMYYFm1c'
SECRETKEY='bGgqSu3wb093ieLuMZWEgsrbFeq54oIZ'
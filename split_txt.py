#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 2:02 下午
# @Author  : CrissChan
# @Site    : https://blog.csdn.net/crisschan
# @File    : split_txt.py
import re
class SplitTxt(object):
    '''
    将一篇文章按照标点覆盖，。？ ！区分成单句（中文标点）
    主要是为了验证，是不是按照一句话生成一次感觉会比较舒服。
    '''
    def __init__(self,txt_dir,txt_file):

        self.txt = txt_dir+txt_file

    def split_aline(self):

        rf = open(self.txt,'r')
        line_list = rf.readlines()
        aline_list=[]
        for aline in line_list:
            aline = aline.replace('\n', '')
            tmp_list=[]
            tmp_list = re.split('，|。|？|！|，',aline)

            aline_list.extend(atemp for atemp in tmp_list if len(atemp)>0)
        return aline_list

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 10:23 上午
# @Author  : CrissChan
# @Site    : https://blog.csdn.net/crisschan
# @File    : ppt2png.py
# @Intro   : ppt 转换成图片。备注转换成文本

import win32com
import win32com.client
import os
import GOLBAL
import PIL.Image as Image
from remover import  Remover
class Ppt2Png(object):

    def __init__(self,ppt_filename,img_dir,txt_dir):
        GOLBAL.__init__()
        try:
            Remover.dir(img_dir)
            Remover.dir(txt_dir)
        except:
            print('无对应文件夹')

        os.mkdir(img_dir)
        os.mkdir(txt_dir)
        self.pptFileName=ppt_filename
        self.img_dir=img_dir
        self.txt_dir = txt_dir
        self.__ppt2png()



    def __ppt2png(self):

        if os.path.exists(self.pptFileName):
            # output_path = output_file(self.pptFileName)  # 判断文件是否存在

            ppt_app = win32com.client.Dispatch('PowerPoint.Application')
            # ppt_app.Visual = 0
            ppt = ppt_app.Presentations.Open(self.pptFileName)  # 打开 ppt

            ppt.SaveAs( self.img_dir, 17)  # 17数字是转为 ppt 转为图片

            slide_count = ppt.Slides.Count
            GOLBAL.set('SLIP_PAGES',slide_count)

            # listForNote = []
            for i in range(1, slide_count + 1):
                shape_count = ppt.Slides(i).Shapes.Count
                notePageRange = ppt.Slides(i)
                slideRange = notePageRange.NotesPage
                noteShape = slideRange.Shapes.Placeholders(2)
                notetxtFrame = noteShape.TextFrame
                textrangestring = notetxtFrame.TextRange
                text1 = textrangestring.Text
                fw = open(self.txt_dir+'\\'+str(i),'w',encoding='utf-8')
                fw.write(text1)
                fw.flush()
                fw.close()


            ppt_app.Quit()  # 关闭资源，退出

    def rename_file(self,dir):

        fileList = os.listdir(dir)

        currentpath = os.getcwd()

        os.chdir(dir)
        for fileName in fileList:
            os.rename(fileName, fileName[3:])
            self.transparent_back(dir, fileName[3:])
        os.chdir(currentpath)


    # 以第一个像素为准，相同色改为透明fileName[:fileName.find('.')]
    def transparent_back(self,img_dir,img_file):
        img = Image.open(img_dir+'\\'+img_file)
        img = img.convert('RGBA')
        L, H = img.size
        color_0 = (255, 255, 255, 255)  # 要替换的颜色
        for h in range(H):
            for l in range(L):
                dot = (l, h)
                color_1 = img.getpixel(dot)
                if color_1 == color_0:
                    color_1 = color_1[:-1] + (0,)
                    img.putpixel(dot, color_1)
        img.save(img_dir+'\\'+img_file[:img_file.find('.')]+'.png')
        os.remove(img_dir+'\\'+img_file)



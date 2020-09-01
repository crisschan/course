#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/28 11:11 下午
# @Author  : CrissChan
# @Site    : https://blog.csdn.net/crisschan
# @File    : save_wav.py
# @intro   : 单词调用tx的tts的api生成符合wav格式的音频编码
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tts.v20190823 import tts_client, models
import uuid
import json
from setting import *
class TTS_TX(object):
    '''
    语音合成免费额度为每月100万字符，相当于一本《西游记》的字数。每月1日重置免费额度。
    接口请求频率限制：20次/每秒。
    合成语音的源文本。中文最大支持600个汉字（全角标点符号算一个汉字），英文最大支持1800个字母（半角标点符号算一个字母）。
    https://cloud.tencent.com/document/product/1073/34093
    '''
    def __init__(self):
        cred = credential.Credential(SECRETID, SECRETKEY)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "tts.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        self.client = tts_client.TtsClient(cred, "ap-beijing", clientProfile)

        self.req = models.TextToVoiceRequest()

    def tts(self,text):
        '''
        文字转语音，返回base64的wav格式
        :param text:
        :return:
        '''
        try:
            self.text = text
            '''
                        -0-云小宁，亲和女声(默认)
                        -1-云小奇，亲和男声
                        -2-云小晚，成熟男声
                        -4-云小叶，温暖女声
                        -5-云小欣，情感女声
                        -6-云小龙，情感男声
                        - 7-云小曼，客服女声（新）
                        1000-智侠，情感男声（新）：小说，新闻
                        1001-智瑜，情感女声（新）：小说，新闻
                        - 1002-智聆，通用女声（新）
                        - 1003-智美，客服女声（新）：
                        1050-WeJack，英文男声（新）
                        1051-WeRose，英文女声（新）
            '''
            params = '{"Text":"' + self.text + \
                     '","SessionId":"' + str(uuid.uuid1()) + \
                     '","ModelType":1,"VoiceType":1000,"Speed":-0.4}'

            self.req.from_json_string(params)

            resp = self.client.TextToVoice(self.req)

            res_tt = resp.to_json_string()
            return json.loads(res_tt)['Audio']
        except TencentCloudSDKException as err:
            return 'error'


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 10:18 上午
# @Author  : CrissChan
# @Site    : https://blog.csdn.net/crisschan


def __init__():
    global __global_dict
    __global_dict={}

def set(key,value):
    __global_dict[key]=value

def get(key):
    try:
        return __global_dict[key]
    except KeyError as e:
        print(e)

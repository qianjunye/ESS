#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sdk import UcloudApiClient
from config import *
from Junye import *
import sys
import time
import json
import time
import subprocess

#高峰期由crontab执行


if __name__=='__main__':
    #读取FastigiumInstance.txt中的实例ID，批量删除
    #建议U提供强制关机API
    FastigiumInstanceID=[]
    for ln in file('FastigiumInstance.txt','rt'):
        FastigiumInstanceID.extend(ln.strip().split(' '))
        print("获取ID")
    for ids in FastigiumInstanceID:
        State=eval(DescribeUHostInstance(Region,ids))
        print(State["UHostSet"][0]["State"])
        if State["UHostSet"][0]["State"] == "Stopped":
            print("Host is stop")
        else:
            StopUHostInstance(Region,ids)
            print "关闭" + ids
            State=eval(DescribeUHostInstance(Region,ids))
            while State["UHostSet"][0]["State"] != "Stopped":
                print ("循环ing")
                time.sleep(5)
                print "等待关闭" + ids
                State=eval(DescribeUHostInstance(Region,ids))
                #StopUHostInstance(Region,ids)
            State=eval(DescribeUHostInstance(Region,ids))
            print(State["UHostSet"][0]["State"])
            a=DeleteUHostInstance(Region,ids)
            print "删除" + ids
            print(a)
    #清空主机池
    subprocess.Popen("echo "" > FastigiumInstance.txt", shell=True)
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sdk import UcloudApiClient
from config import *
from function import *
import sys
import time
import json
import time

#高峰期由crontab执行

#高峰期后由cront做执行操作
if __name__=='__main__':
    #读取FastigiumInstance.txt中的实例ID，批量删除
    #建议U提供强制关机API
    FastigiumInstanceIDall=[]
    FastigiumInstanceID=[]
    for ln in file('FastigiumInstance.txt','rt'):
        FastigiumInstanceIDall.extend(ln.strip().split(' '))
        print("获取ID")
    for ids in FastigiumInstanceIDall:
        Count = eval(DescribeUHostInstance(Region,ids))
        if Count["TotalCount"]==1:
            FastigiumInstanceID.append(ids)
    for ids in FastigiumInstanceID:
        print(ids)
        b=DescribeUHostInstance(Region,ids)
        print(b)
        print "is"
        State=eval(DescribeUHostInstance(Region,ids))
        a=type(State)
        print(a)
        print(State["UHostSet"][0]["State"])
        if State["UHostSet"][0]["State"] == "Stopped":
            print("Host is stop")
            a=DeleteUHostInstance(Region,ids)
            print "删除" + ids
            print(a)
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
            #print "删除" + ids
            print(a)
    Clear_File = open('FastigiumInstance.txt', 'w')
    Clear_File.write("")
    Clear_File.close( )
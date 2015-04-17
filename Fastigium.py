#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sdk import UcloudApiClient
from config import *
from function import *
import sys
import time
import json


#高峰期由crontab执行

#生成主机且自动加入SUB，
if __name__=='__main__':
    #镜像名用于区分主机类型
    InstanceName="Fastigium"+time.strftime('%Y-%m-%d_%H:%M:%S',time.localtime(time.time()))
    #根据config.py中的配置，确定是复制slaver还是从镜像生成
    if Source == "instance":
        ImageName=ImageNamePrefix+time.strftime('%Y-%m-%d_%H:%M:%S',time.localtime(time.time()))
        ImageID=eval(CreateCustomImage(Region,slaver,ImageName))["ImageId"]
        #根据config.py中的配置，确定硬件配置采用slaver的还是自定义的
        if HW == "copy":
            HardWareInFo=GetHWInfo(Region,slaver)
            newinstance=CreateUHostInstance(Region,ImageID,HardWareInFo["CPUInfo"],HardWareInFo["MemInfo"],InstanceName)
            newinstanceid=eval(newinstance)["UHostIds"][0]
        else:
            newinstance=CreateUHostInstance(Region,ImageID,CPUInFo,MemInFo,InstanceName)
            newinstanceid=eval(newinstance)["UHostIds"][0]
    else:
        GetImageID=SearchCustomImageId(Region,SourceImageName)
        if HW == "copy":
            HardWareInFo=GetHWInfo(Region,slaver)
            newinstance=CreateUHostInstance(Region,GetImageID,HardWareInFo["CPUInfo"],HardWareInFo["MemInfo"],InstanceName)
            newinstanceid=eval(newinstance)["UHostIds"][0]
        else:
            newinstance=CreateUHostInstance(Region,GetImageID,CPUInFo,MemInFo,InstanceName)
            newinstanceid=eval(newinstance)["UHostIds"][0]
    FastigiumInstanceFile=open(FastigiumInstance,'a')
    FastigiumInstanceFile.write(newinstanceid+'\n')
    FastigiumInstanceFile.close()
    re = AllocateBackend(Region,ULBID,VserverID,newinstanceid)
    print re



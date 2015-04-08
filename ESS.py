#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sdk import UcloudApiClient
from config import *
from function import *
import sys
import time
import json
import time
import subprocess


if __name__=='__main__':
    while(1):
        Metric=GetMetric(360,Region,slaver)#时间精度不够，60秒可能获取不到数据建议拉长，得到的360秒内的硬件平均值
        HW=DealMetric(Metric)
        if HW[0] > CPUThreshold:
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
            FastigiumInstanceFile=open(ESSInstance,'a')
            FastigiumInstanceFile.write(newinstanceid+'\n')
            FastigiumInstanceFile.close()
        time.sleep(TimerRange)
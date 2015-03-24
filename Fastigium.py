#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sdk import UcloudApiClient
from config import *
import sys
import time
import json


#高峰期由crontab执行

#获取参数，执行请求URL
def Request(Parameters):
    rg_length = len(sys.argv)
    ApiClient = UcloudApiClient(base_url, public_key, private_key)
    response = ApiClient.get("/", Parameters)
    return json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))

#输入环境与主机ID查机器信息
def DescribeUHostInstance(Region,UHostId):
    Parameters={
                "Action":"DescribeUHostInstance",
                "Region":Region,
                "UHostIds.0":UHostId,
               }
    return Request(Parameters)

def GetHWInfo(Region,slaver):
    InstanceInfo = eval(DescribeUHostInstance(Region,slaver))
    CPUInfo = InstanceInfo["UHostSet"][0]["CPU"]
    MemInfo = InstanceInfo["UHostSet"][0]["Memory"]
    return {"CPUInfo":CPUInfo,"MemInfo":MemInfo}

#输入环境与主机ID查镜像名
def CreateCustomImage(Region,UHostId,ImageName):
    Parameters={
                "Action":"CreateCustomImage",
                "Region":Region,
                "UHostId":UHostId,
                "ImageName":ImageName,
               }
    return Request(Parameters)

#输入镜像名查镜像ID
def SearchCustomImageId(Region,ImageName):
    Parameters = {
                    "Action":"DescribeImage",
                    "Limit":"100",
                    "ImageType":"Custom",
                    "Region":Region,
                }
    Image_Info=Request(Parameters)
    #print Image_Info
    Image_Info=eval(Image_Info)
    Image_Info=Image_Info["ImageSet"]
    a=type(Image_Info)
    for images in Image_Info:
        if images["ImageName"] == ImageName:
            return images["ImageId"]
    if len(image_ID) != 1:
        print "Get ID ERROR"
        return "NULL"

def CreateUHostInstance(Region,ImageId,CPU,Memory,Name):
    ApiClient = UcloudApiClient(base_url, public_key, private_key)
    Parameters={
            "Action":"CreateUHostInstance",
            "Region":Region,
            "ImageId":ImageId,
            "LoginMode":"Password",
            "Password":"VWNsb3VkUGFzc3dk",
            "CPU":CPU,
            "Memory":Memory,
            "Name":Name,
            "ChargeType": "Dynamic",
            }
    return Request(Parameters)



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



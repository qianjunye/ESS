#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sdk import UcloudApiClient
from config import *
import sys
import time
import json



#获取参数，执行请求URL
def Request(Parameters):
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

def DeleteUHostInstance(Region,UHostId):
    Parameters={
                "Action":"TerminateUHostInstance",
                "Region":Region,
                "UHostId":UHostId,
               }
    return Request(Parameters)

def StopUHostInstance(Region,UHostId):
    Parameters={
                "Action":"StopUHostInstance",
                "Region":Region,
                "UHostId":UHostId,
               }
    return Request(Parameters)
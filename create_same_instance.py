#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sdk import UcloudApiClient
from config import *
import sys
import time
import json

#镜像命名规则


#输入环境与主机ID查机器信息
def DescribeUHostInstance(Region,UHostId):
    arg_length = len(sys.argv)
    ApiClient = UcloudApiClient(base_url, public_key, private_key)
    Parameters={
                "Action":"DescribeUHostInstance",
                "Region":Region,
                "UHostIds.0":UHostId,
               }
    response = ApiClient.get("/", Parameters);
    print json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))
    

#输入环境与主机ID查镜像名
def CreateCustomImage(Region,UHostId,ImageName):
    arg_length = len(sys.argv)
    ApiClient = UcloudApiClient(base_url, public_key, private_key)
    Parameters={
                "Action":"CreateCustomImage",
                "Region":Region,
                "UHostId":UHostId,
                "ImageName":ImageName,
               }
    response = ApiClient.get("/", Parameters);
    print json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))
    

#输入镜像名查镜像ID
def FindCustomImageId(Region,ImageName):
    arg_length = len(sys.argv)
    ApiClient = UcloudApiClient(base_url, public_key, private_key)
    Parameters = {
                    "Action":"DescribeImage",
                    "Limit":"100",
                    "ImageType":"Custom",
                    "Region":Region,
                }
    response = ApiClient.get("/", Parameters);
    #print json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))
    Image_Info=json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))
    #print Image_Info
    Image_Info=eval(Image_Info)
    Image_Info=Image_Info["ImageSet"]
    a=type(Image_Info)
    for images in Image_Info:
        if images["ImageName"] == ImageName:
            return ["ImageId"]
    if len(image_ID) != 1:
        print "Get ID ERROR"
        return "NULL"


if __name__=='__main__':
    #DescribeUHostInstance("cn-north-03","uhost-ikzxb3")
    #ImageName="Junye"+time.strftime('%Y-%m-%d_%H:%M:%S',time.localtime(time.time()))
    #print ImageName
    #CreateCustomImage(Region,"uhost-ikzxb3",ImageName)
    ID = FindCustomImageId(Region,"william")
    print(ID)

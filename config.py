#-*- encoding: utf-8 -*-
#配置公私钥
public_key  = "ucloudxxxxxxx"
private_key = "3baxxxxxxxxxx"
#配置检查所在可用区
Region = "cn-north-03"
base_url    = "https://api.ucloud.cn"

ImageNamePrefix = "UcloudImage" #镜像名前缀，可以随意设置
#推荐架构：默认空闲时有两台主机在运行，分别为Master与slaver，如只有一台可将两个变量的设置相同
Master	=	""
slaver	=	""

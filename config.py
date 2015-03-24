#-*- encoding: utf-8 -*-
#配置公私钥
public_key  = "ucloudxxxxxxx"
private_key = "3baxxxxxxxxxx"
#配置检查所在可用区
Region = "cn-north-03"
base_url    = "https://api.ucloud.cn"

ImageNamePrefix = "UcloudImage" #镜像名前缀，可以随意设置
Source = "instance"             #确定是从实例生成主机，还是从镜像生成主机值为instance或者image,


#推荐架构：默认空闲时有两台主机在运行，分别为Master与slaver，如只有一台可将两个变量的设置相同
#当Source值为instance时使用slaver复制新主机
Master	=	""
slaver	=	""


#当Source为image时用下面的镜像名生成机器
SourceImageName="UcloudImage2015-03-24_14:26:34"
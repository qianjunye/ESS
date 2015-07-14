#-*- encoding: utf-8 -*-
#配置公私钥
public_key  = "ucloudxxxxxxx"
private_key = "3baxxxxxxxxxx"
#配置检查所在可用区
Region = "cn-north-03"
base_url    = "https://api.ucloud.cn"

ImageNamePrefix = "UcloudImage" #镜像名前缀
Source = "image"             #确定是从实例生成主机，还是从镜像生成主机值为instance或者image,

#存储 脚本执行生成的机器ID列表
FastigiumInstance="FastigiumInstance.txt"
ESSInstance="ESSInstance.txt"
#推荐架构：默认空闲时有两台主机在运行，分别为Master与slaver，如只有一台可将两个变量的设置相同
#当Source值为instance时使用slaver复制新主机
Master	=	"uhost-x13e4e"
slaver	=	"uhost-x13e4e"

#当Source为image时用下面的镜像名生成机器
SourceImageName="william"

#新机器的硬件信息
HW = "copy"                     #值为copy或者defined，如果值为copy则与slaver的相同，其他值则使用下面的指定值
CPUInFo="1"
MemInFo="2048"                     #MB 范围[2048,65536]， 步长：2048， 默认值：8192

#监控阈值
TimerRange = 500                #单位秒，Ucloud的监控阈值如小于60经常会获取不到数据
CPUThreshold = 80
MemThreshold = 90


#高峰期时间设定
FastigiumTime = [["7:30","9:30"],["16:30","17:30"]]
#格式 [["起始时间","结束时间"],["起始时间","结束时间"]] 二维列表，可以按规添加时间时间段



ULBID = "ulb-kgf3da"
VserverID="9d33b735-207b-4db3-85f6-012ccc71f591"

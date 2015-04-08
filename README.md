    Elastic Scaling Service For Ucloud
    通过Ucloud 的API实现弹性伸缩服务,高负载时集群自动部署新机器并且分担负载
    CustomImage & SLB

    使用说明：
        执行cront_init.py 生成"/etc/cron.d/Uhost"文件并且重启cronttab服务，引导
        ESS.py执行
            会在预计的高峰期生成主机并且在的指定时间释放
            ESS.py每分钟获取一次最近指定时间内的CPU值，如果过设定的阈值则创建主机。
        
    
待完善
    UCloud的监控代理不稳定时常获取不到数据，需要考虑更好的办法绕过，或者找替代方法
    删除主机时如果需要先关机，有时软关机会卡住
    ESS生成的主机删除策略
    本地日志功能
        
    



    基于原Ucloud Python SDK 
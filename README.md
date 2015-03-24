    Elastic Scaling Service For Ucloud
    通过Ucloud 的API实现弹性伸缩服务,高负载时集群自动部署新机器并且分担负载
    CustomImage & SLB

    slaver的自动复制 （Doing）create_same_instance.py
        create_same_instance.py 通过crontab定时执行（预估的高峰期）
        ESS.py                  长期执行，监控服务器负载，高过指定值后生成新机器
    Master与 slaver
    负载监控
    slaver生成后自动加入ULB



    基于原Ucloud Python SDK 
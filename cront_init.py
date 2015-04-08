#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'junye'
from config import *
import os

if __name__=='__main__':
	CrontString = ""
	for time in FastigiumTime:
		StartTime = time[0].split(':')
		EndTime = time[1].split(':')
		StartString = StartTime[1]+" "+StartTime[0]+" "+ "* * * root /usr/bin/python /root/SDK_Ucloud/Fastigium.py" +'\n'
		EndString = EndTime[1] +" "+ EndTime[0] + " "+ "* * * root /usr/bin/python /root/SDK_Ucloud/delete_instance.py" +'\n'
		CrontString = CrontString + StartString +EndString


	print(CrontString)

	Crontab = "/etc/cron.d/Uhost"
	CronFile=open(Crontab,'w')
	CronFile.write(CrontString)
	CronFile.close()
	os.system('service cron restart')

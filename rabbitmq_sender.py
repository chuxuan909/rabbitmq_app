#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os,sys
import app_rabbitmq
if __name__ == '__main__':
    package_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(package_path)
sender = app_rabbitmq.App_rabbitmq()
sender.input('rqm402.1','Huluwa')
sender.close()
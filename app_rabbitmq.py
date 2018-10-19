#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Rabbitmq的简单操作
import pika
HOST='192.168.0.211'
PORT=5672
class App_rabbitmq(object):
    def __init__(self):
        '''连接rabbitmq
           创建管道
        '''
        self.__con=pika.BlockingConnection(pika.ConnectionParameters(HOST,port=PORT))
        self.__channles=self.__con.channel()
    def callback(self,ch, method, properties, body):
        '''
        回调函数
        '''
        body = str(body,'utf-8')
        print("Recv: %r" % body)
    def input(self,q_name,q_message):
        '''
        发送消息到队列
        '''
        self.__channles.queue_declare(queue=q_name)
        self.__channles.basic_publish(exchange='',
                                      routing_key=q_name,
                                      body=q_message)
    def get_message(self,q_name):
        '''
        接收消息
        '''
        self.__channles.queue_declare(queue=q_name)
        self.__channles.basic_consume(self.callback,
                                      queue=q_name,
                                      no_ack=False)
    def begin_recive(self):
        '''
        开始接收消息
        :return:
        '''
        self.__channles.start_consuming()
    def close(self):
        '''
        关闭连接
        '''
        self.__con.close()

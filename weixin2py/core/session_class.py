#coding:utf-8
#in folder 'core'
#session classes by winkidney,used to store session status
import datetime
class WeiSession(object):
    '''微信助手会话类，用来存储用户的会话状态'''
    def __init__(self):
        self.lastcommit_time = datetime.datetime.now()
        self.status = u''
    def update(self):
        self.lastcommit_time = datetime.datetime.now()
    def menu_back(self,):
        self.status = self.status[0:-2]
    def menu_add(self,menu_obj):
        self.status = self.status+menu_obj
    def exit(self):
        self.status =''
class WeiChatSession(object):
    pass
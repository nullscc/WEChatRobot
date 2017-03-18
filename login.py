# coding: utf-8
import itchat
import sys
from itchat.content import *
import robot
import time

myrobot = robot.tulingrobot()

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    # print "[+]   From " + msg['FromUserName']+ "to" + msg['ToUserName'] +" : " +msg['Text']
    userid = msg['FromUserName']

    res = myrobot.switch(msg['Content'], userid)
    if res:
        # itchat.send(res,msg['FromUserName'])
        itchat.send(res,toUserName='filehelper')
    else:
        if myrobot.getRobotStatus(userid):
            req = myrobot.tuling_auto_replay(msg['FromUserName'],msg['Text'])
            # itchat.send(req,msg['FromUserName'])
            itchat.send(req,toUserName='filehelper')

def main():
    itchat.auto_login(enableCmdQR=2, hotReload=True)
    itchat.run()

#itchat.auto_login(enableCmdQR=True )
if __name__ == '__main__':
    main()




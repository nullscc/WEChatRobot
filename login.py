# coding: utf-8
import itchat
import sys
from itchat.content import *
import robot

myrobot = robot.tulingrobot()

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    print "[+]   From " + msg['FromUserName']+ " : " +msg['Text']

    if (msg['FromUserName'] == msg['ToUserName']):
        req = myrobot.switch(msg['Content'])
        itchat.send(req,msg['FromUserName'])
    else:
        if(myrobot.getRobotStatus()):
            req = myrobot.tuling_auto_replay(msg['FromUserName'],msg['Text'])
            itchat.send(req,msg['FromUserName'])
            print "[-]   [Robot] : " + req
        #else :
        #    itchat.send(u"收到啦~",msg['FromUserName'])

def main(mod=False):
    itchat.auto_login(enableCmdQR=mod)
    itchat.run()

#itchat.auto_login(enableCmdQR=True )
if __name__ == '__main__':
    if len(sys.argv) < 2:
        main()
    else:
        if sys.argv[1].startswith('-'):
            option = sys.argv[1]
            if option == '-cmdQR':
                main(True)
            else:
                print '''
           \n[+]  Use: 'python login.py cmdQR' to enable cmd QRcode.
           \n[+]  Use: 'python login.py ' and Scan QRcode to login
           '''




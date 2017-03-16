# coding:utf-8
import requests
import json

class tulingrobot :
    def __init__(self):

        self.robot_status = True

        with open("key.txt",'r') as fi :
            self.key = fi.readline()
        self.key

    def getRobotStatus(self):
        return self.robot_status

    def setRobotStatus(self,statue):
        self.robot_status = statue

    def tuling_auto_replay(self,uid,msg):
        tuling_key = self.key
        if tuling_key:
            url = "http://www.tuling123.com/openapi/api"
            user_id = uid.replace('@', '')[:30]
            # body = {'key': tuling_key, 'info': msg.encode('utf8'), 'userid': user_id}
            body = {'key': tuling_key, 'info': msg, 'userid': user_id}
            r = requests.post(url, data=body)
            respond = json.loads(r.text)
            result = ''
            if respond['code'] == 100000:
                result = respond['text'].replace('<br>', '  ')
                result = result.replace(u'\xa0', u' ')
            elif respond['code'] == 200000:
                result = respond['url']
            elif respond['code'] == 302000:
                for k in respond['list']:
                    result = result + u"[" + k['source'] + u"] " +\
                    k['article'] + "\t" + k['detailurl'] + "\n"
            else:
                result = respond['text'].replace('<br>', '  ')
                result = result.replace(u'\xa0', u' ')
                print '    ROBOT:', result
            return result
        else:
            return u"知道啦"

    def switch(self,msg):

        msg_data = msg
        stop_cmd = [u'退下', u'走开', u'关闭', u'关掉', u'休息', u'滚开']
        start_cmd = [u'出来', u'启动', u'工作']

        for i in stop_cmd:
            if i == msg_data :
                if self.getRobotStatus() :
                    self.setRobotStatus(False)
                    return u"关闭机器人"
                else:
                    return u"机器人已关闭"

        for i in start_cmd:
            if i == msg_data:
                if self.getRobotStatus() :
                    return u"机器人已开启"
                else :
                    self.setRobotStatus(True)
                    return u"开启机器人"

        return u"命令无效哦"


if __name__ == "__main__":
    print "[+]  starting robot script"


#check model
#bot = robot()
#print bot.tuling_auto_replay('','你是谁')
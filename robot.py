# coding:utf-8
import requests
import json
robotCtrl = {}

class tulingrobot :
    def __init__(self):

        with open("key.txt",'r') as fi :
            self.key = fi.readline()
        self.key

    def getRobotStatus(self,userid):
        if not (userid in robotCtrl):
            self.setRobotStatus(userid, True)
        return robotCtrl[userid]

    def setRobotStatus(self,userid, sw):
        robotCtrl[userid] = sw

    def switch(self,msg, userid):
        msg_data = msg
        stop_cmd = [u'退下', u'走开', u'关闭', u'关掉', u'休息', u'滚开']
        start_cmd = [u'出来', u'启动', u'工作']

        for i in stop_cmd:
            if i == msg_data :
                if self.getRobotStatus(userid) :
                    self.setRobotStatus(userid, False)
                    return u"关闭机器人"
                else:
                    return u"机器人已关闭"

        for i in start_cmd:
            if i == msg_data:
                if self.getRobotStatus(userid) :
                    return u"机器人已开启"
                else :
                    self.setRobotStatus(userid, True)
                    return u"开启机器人"

        return False

    def tuling_auto_replay(self,uid,msg):
        tuling_key = self.key
        if tuling_key:
            url = "http://www.tuling123.com/openapi/api"
            user_id = uid.replace('@', '')[:30]
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
            return u"请通知微信主人设置appkey"

if __name__ == "__main__":
    print "[+]  starting robot script"

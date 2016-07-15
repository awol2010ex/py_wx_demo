from app.weixin.BaseWeixinPlugin import BaseWeixinPlugin
import http.client, urllib.parse
import json
from datetime import datetime
#天气接口
class WeatherPlugin(BaseWeixinPlugin):
    #检查是否符合接口
    def check(self,msgtype ,content ,appuuid ):
        if msgtype=='text' and  content  and  str(content).startswith('天气') :
            return True
        else:
            return False
    #回复
    def reply(self,msgtype ,content ,appuuid ):
        cityname=str(content)[2:]
        print(cityname)
        ret={}
        print(datetime.now())
        try:
            conn = http.client.HTTPConnection("localhost",810)  
            conn.set_tunnel("apis.baidu.com")
            conn.request("GET", "/apistore/weatherservice/cityname?"+urllib.parse.urlencode({"cityname":cityname}), headers={"apikey":""}
            )
            r = conn.getresponse()
            s=(r.read()).decode('utf-8')
            print(s)
            ret=json.loads(s)
        except:
            return "超时"
        print(datetime.now())
        return ret["retData"]["weather"]

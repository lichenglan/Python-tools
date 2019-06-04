# -*-coding:utf-8 -*-
# 驾校一点通
import requests
import time
import json
import urllib

import webbrowser

from requests import HTTPError

imeiList = {'866117035052641', '860916033907532'}
html = ''
currentTime = 0
urlHeader = 'https://richmanapi.jxedt.com/api/ad/1/7.4.1/8/v2?packagename=com.jxedt&lon=116.355697&osv=6.0.1&adwidth=640&kemutype=1&cartype=0&imei=860916033907532&version=7.4.1&type=practopbanad&channel=8&aaid=0&androidid=c8436223ae65d579&time='
urlEnd = '&cityid=1&mac=02:00:00:00:00:00&screenheight=1280&issupportdeeplink=1&net=1&density=320.0&productid=1&os=android&useragent=Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36&carriername=-1&make=vivo&screenwidth=720&adheight=100&lat=39.981753&model=vivo Y66'

currentTime = int(time.time())
print('currentTime ==>', currentTime)
url = urlHeader + str(currentTime) + urlEnd
requests.packages.urllib3.disable_warnings()
for x in range(100):
  try:
    res = requests.get(url, verify=False)
    print('第' + str(x) + '次获取广告信息====>' + url)
    print('状态码==>', res.status_code)
    print('报文头==>', res.headers)
    print('body ==>', res.text)
    resp = json.loads(res.text)

    if not resp['result'] is None and not resp['result']['practopbanad'] is None and not \
        resp['result']['practopbanad']['data'] is None:

      # 命名生成的html
      GEN_HTML = "adver.html"
      f = open(GEN_HTML, 'w')

      if resp['result']['practopbanad']['adtype'] == 'html5':
        html = resp['result']['practopbanad']['data'][0]['html']

      elif resp['result']['practopbanad']['adtype'] == 'native':
        html = """
        <html>
        <head></head>
        <body>
        <img src=%s>
        </body>
        </html>""" % (resp['result']['practopbanad']['data'][0]['imageurl'])

      f.write(html)
      f.close()
      # 运行完自动在网页中显示
      # webbrowser.open(GEN_HTML, new=1)
      webbrowser.open(GEN_HTML, new=0, autoraise=True)

    time.sleep(2)
    currentTime = int(time.time())
    url = urlHeader + str(currentTime) + urlEnd
  except HTTPError as e:
    print('出现异常==>', e)
  except AttributeError as e:
    print("Tag was not found")

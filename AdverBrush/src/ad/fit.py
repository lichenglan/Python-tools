# -*-coding:utf-8 -*-
# fit 健身头条（6）

import requests
import time
import json
import webbrowser

# 请求的时间戳
currentTime = int(time.time())

# 请求头
requestHeaders = {
  'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
  'content-type': 'application/json',
  'Host': 's.ad4.com.cn',
  'Connection': 'Keep-Alive',
  'Accept-Encoding': 'gzip',
  'Content-Length': '555'
}
# 请求body体
requestBody = {"appkey": "76bfdd1257ba6492", "pid": "1871204", "v": "2.1a", "s": 1, "timestamp": 1559294269296,
               "device": {"adid": "", "anid": "d70ac4e6752e71f9", "brand": "vivo",
                          "ua": "Mozilla\/5.0 (Linux; Android 6.0.1; vivo Y66 Build\/MMB29M; wv) AppleWebKit\/537.36 (KHTML, like Gecko) Version\/4.0 Chrome\/51.0.2704.81 Mobile Safari\/537.36",
                          "density": "2.0", "imei": "866117035052641", "imsi": "null", "lang": "zh", "lat": "-1.0",
                          "lon": "-1.0", "mac": "1C:DA:27:D3:40:67", "mcc": "", "mnc": "", "model": "vivo Y66",
                          "orientation": "0", "osv": "6.0.1", "os": 1, "sh": 1280, "sw": 720, "type": 0,
                          "connection": 1}}
# 请求的url
url = 'http://s.ad4.com.cn/ad/get'

html = ''

for x in range(100):
  res = requests.post(url, json.dumps(requestBody), requestHeaders)
  print('第' + str(x) + '次获取广告数据 ===========>')
  print('状态码==>', res.status_code)
  print('body ==>', res.text)
  resp = json.loads(res.text)

  if resp.get('ads') == None:
    continue

  # showreport
  print(len(resp['ads'][0]['show_report']))
  for x in range(len(resp['ads'][0]['show_report'])):
    if resp['ads'][0]['show_report'][x] != '':
      print(resp['ads'][0]['show_report'][x])
      requests.get(resp['ads'][0]['show_report'][x])

  # 命名生成的html
  GEN_HTML = "fit.html"
  f = open(GEN_HTML, 'w')
  if resp.get('ads') and resp.get('ads')[0].get('html'):
    print('广告类型为 html========>')
    html = resp.get('ads')[0].get('html')
  elif resp.get('ads') and resp.get('ads')[0].get('image_url'):
    print('广告类型为图片=====>')
    html = """
       <html>
       <head></head>
       <body> 
       <img src=%s>
       </body>
       </html>""" % (resp['ads'][0]['image_url'][0])
  f.write(html)
  f.close()
  # 运行完自动在网页中显示
  webbrowser.open(GEN_HTML, new=0, autoraise=True)

  # 重新赋值
  time.sleep(10)
  currentTime = int(time.time())
  requestBody['timestamp'] = currentTime

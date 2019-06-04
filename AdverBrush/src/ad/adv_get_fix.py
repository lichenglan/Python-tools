# -*- coding:utf-8 -*-
import os

import requests
import time
import json
import webbrowser
from requests import HTTPError

requests.packages.urllib3.disable_warnings()

# 网络请求的时间戳
currentTime = int(time.time())
# 要展示的 html 页面
html = ''

# 百度视频 url 前段 (mac,device=android&os=1&os_version=23&screen_width=720&screen_height=1280&imei=866117035052641
baiduUrlHeader = 'http://app.video.baidu.com/adver/?terminal=adnative&adver_version=0.0.0&position=stop&works_id=short_video_e451c7d7c5a7118c65a725a8753324c9&site=http%3A%2F%2Fbaishi.baidu.com%2Fwatch%2F7788471627219284212.html&online=1&video_type=normal&play_channel=&block_sign=amuse&dpi=320&player_style=card&device=android&os=1&os_version=23&screen_width=720&screen_height=1280&imei=866117035052641&locale=zh_CN&vendor=vivo&model=vivo+Y66&android_id=d70ac4e6752e71f9&connection_type=100&operator_type=0&orientation=p&uniqueid=2b60c2a37c60dbfd6626f617b5d78779&mtj_cuid=5E9A7E636F8C5565B2281683B66E45C4%7C146250530711668&mtj_timestamp=1559299005956&mac_address=02:00:00:00:00:00&ados_ver=6.0.1&dev=vivoY66&lf=eyJsb25naXR1ZGUiOiIxMTYuMzU1NjIiLCJsYXRpdHVkZSI6IjM5Ljk4MTc3In0%3D%0A&channel=563o&version=8.10.1&_smc=0&_irt=0&_adsdk=23&fstapktime='

# fit健身头条请求头
fitHeaders = {
  'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
  'content-type': 'application/json',
  'Host': 's.ad4.com.cn',
  'Connection': 'Keep-Alive',
  'Accept-Encoding': 'gzip',
  'Content-Length': '555'
}
# fit健身头条请求body体
fitBody = {"appkey": "76bfdd1257ba6492", "pid": "1871204", "v": "2.1a", "s": 1, "timestamp": 1559294269296,
           "device": {"adid": "", "anid": "d70ac4e6752e71f9", "brand": "vivo",
                      "ua": "Mozilla\/5.0 (Linux; Android 6.0.1; vivo Y66 Build\/MMB29M; wv) AppleWebKit\/537.36 (KHTML, like Gecko) Version\/4.0 Chrome\/51.0.2704.81 Mobile Safari\/537.36",
                      "density": "2.0", "imei": "866117035052641", "imsi": "null", "lang": "zh", "lat": "-1.0",
                      "lon": "-1.0", "mac": "1C:DA:27:D3:40:67", "mcc": "", "mnc": "", "model": "vivo Y66",
                      "orientation": "0", "osv": "6.0.1", "os": 1, "sh": 1280, "sw": 720, "type": 0,
                      "connection": 1}}

# 行家说
hangjiashuoHeaders = {
  'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
  'content-type': 'application/json',
  'Host': 's.lmstyle.cn',
  'Connection': 'Keep-Alive',
  'Accept-Encoding': 'gzip',
  'Content-Length': '555'
}
hangjiashuoBody = {"appkey": "7f4756ead2bb3e88", "pid": "1737502", "v": "2.1a", "s": 1, "timestamp": currentTime,
                   "device": {"adid": "", "anid": "d70ac4e6752e71f9", "brand": "vivo",
                              "ua": "Mozilla\/5.0 (Linux; Android 6.0.1; vivo Y66 Build\/MMB29M; wv) AppleWebKit\/537.36 (KHTML, like Gecko) Version\/4.0 Chrome\/51.0.2704.81 Mobile Safari\/537.36",
                              "density": "2.0", "imei": "866117035052641", "imsi": "null", "lang": "zh", "lat": "-1.0",
                              "lon": "-1.0", "mac": "1C:DA:27:D3:40:67", "mcc": "", "mnc": "", "model": "vivo Y66",
                              "orientation": "0", "osv": "6.0.1", "os": 1, "sh": 1280, "sw": 720, "type": 0,
                              "connection": 1}}

# 驾校一点通
jiaxiaoHeader = 'https://richmanapi.jxedt.com/api/ad/1/7.4.1/8/v2?packagename=com.jxedt&lon=116.355697&osv=6.0.1&adwidth=640&kemutype=1&cartype=0&imei=860916033907532&version=7.4.1&type=practopbanad&channel=8&aaid=0&androidid=c8436223ae65d579&time='
jiaxiaoEnd = '&cityid=1&mac=02:00:00:00:00:00&screenheight=1280&issupportdeeplink=1&net=1&density=320.0&productid=1&os=android&useragent=Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36&carriername=-1&make=vivo&screenwidth=720&adheight=100&lat=39.981753&model=vivo Y66'


class GlobalCount:
  def __init__(self):
    self.baiduCount = 0
    self.fitCount = 0
    self.hangjiashuoCount = 0
    self.jiaxiaoCount = 0


GL = GlobalCount()


# 获取当前时间戳
def getCurrentTime():
  return int(time.time())


# 设置曝光的 html 数据
def setHtml(name, adType, adData):
  # 命名生成的html
  GEN_HTML = name
  f = open(GEN_HTML, 'w')
  if adType == 'img':
    html = """
                     <html>
                     <head></head>
                     <body>
                     <img src=%s>
                     </body>
                     </html>""" % (adData)
  else:
    html = adData
  f.write(html)
  f.close()
  # 运行完自动在网页中显示
  ret = webbrowser.open(GEN_HTML, new=0, autoraise=True)
  print("open ret type:", type(ret))


# 获取百度视频中的广告（暂停时刷新广告）
def getBiduVideoAd():
  url = baiduUrlHeader + str(getCurrentTime())
  try:
    res = requests.get(url, verify=False)
    GL.baiduCount += 1
    print("《百度视频》请求次数 ========>", GL.baiduCount)
    print('状态码==>', res.status_code)
    print('报文头==>', res.headers)
    print('body ==>', res.text)
    resp = json.loads(res.text)

    if resp['reqtime'] is not None:
      requests.get(resp['reqtime'])

    if resp['data'] is not None and resp['data']['stop'] is not None and len(resp['data']['stop']) >= 2 and \
        resp['data']['stop'][1]['data'] is not None and resp['data']['stop'][1]['data'][0] is not None and \
        resp['data']['stop'][1]['data'][0]['request']:
      requests.get(resp['data']['stop'][1]['data'][0]['request'])

    if resp['data']['stop'][1]['category'] == 'dsp':
      setHtml('baiduVideo.html', 'img', resp['data']['stop'][1]['data'][0]['multi_img'][0])

    # 重新赋值
    time.sleep(2)
    url = baiduUrlHeader + str(getCurrentTime())
  except HTTPError as e:
    print('出现异常==>', e)
    # 重新请求
    time.sleep(100)
    getBiduVideoAd()
  except AttributeError as e:
    print("Tag was not found")


# 获取 fit 健身头条广告
def getFitAd():
  fitUrl = 'http://s.ad4.com.cn/ad/get'
  try:
    res = requests.post(fitUrl, json.dumps(fitBody), fitHeaders)
    GL.fitCount += 1
    print("《fit 健身头条》请求次数 ========>", GL.fitCount)
    print('状态码==>', res.status_code)
    print('body ==>', res.text)
    resp = json.loads(res.text)

    if resp.get('ads') is not None and len(resp['ads']) > 0 and resp['ads'][0]['show_report'] is not None and len(
        resp['ads'][0]['show_report']) > 0:
      for i in range(len(resp['ads'][0]['show_report'])):
        if resp['ads'][0]['show_report'][i] != '':
          print(resp['ads'][0]['show_report'][i])
          requests.get(resp['ads'][0]['show_report'][i])

    if resp.get('ads') and resp.get('ads')[0].get('html'):
      print('广告类型为 html========>')
      setHtml('fit.html', 'html', resp.get('ads')[0].get('html'))
    elif resp.get('ads') and resp.get('ads')[0].get('image_url'):
      print('广告类型为图片=====>')
      setHtml('fit.html', 'img', resp['ads'][0]['image_url'][0])

    # 重新赋值
    time.sleep(2)
    fitBody['timestamp'] = getCurrentTime()

  except Exception as e:
    print('出现异常==>', e)
    # 重新请求
    time.sleep(100)
    getFitAd()


# 获取行家说说的广告
def getHangjiashuoAd():
  url = 'http://s.lmstyle.cn/ad/get'
  try:
    res = requests.post(url, json.dumps(hangjiashuoBody), hangjiashuoHeaders)
    GL.hangjiashuoCount += 1
    print("《行家说说》请求次数 ========>", GL.hangjiashuoCount)
    print('状态码==>', res.status_code)
    print('body ==>', res.text)
    resp = json.loads(res.text)

    for i in range(len(resp['ads'][0]['show_report'])):
      if resp['ads'][0]['show_report'][i] != '':
        print(resp['ads'][0]['show_report'][i])
        requests.get(resp['ads'][0]['show_report'][i])

    if resp.get('ads') and resp.get('ads')[0].get('html'):
      print('广告类型为 html========>')
      setHtml('hangjiashuo.html', 'html', resp.get('ads')[0].get('html'))
    elif resp.get('ads') and resp.get('ads')[0].get('image_url'):
      print('广告类型为图片=====>')
      setHtml('hangjiashuo.html', 'img', resp['ads'][0]['image_url'][0])

    # 重新赋值
    time.sleep(2)
    hangjiashuoBody['timestamp'] = getCurrentTime()
  except Exception as e:
    print('出现异常==>', e)
    # 重新请求
    time.sleep(100)
    getHangjiashuoAd()
  except AttributeError as e:
    print("Tag was not found")


# 获取驾校一点通广告
def getJiaxiaoAd():
  url = jiaxiaoHeader + str(currentTime) + jiaxiaoEnd
  try:
    res = requests.get(url, verify=False)
    GL.jiaxiaoCount += 1
    print("《驾校一点通广告》请求次数 ========>", GL.jiaxiaoCount)
    print('状态码==>', res.status_code)
    print('报文头==>', res.headers)
    print('body ==>', res.text)
    resp = json.loads(res.text)

    if resp['result'] is not None and resp['result']['practopbanad'] is not None and \
        resp['result']['practopbanad']['data'] is not None:
      if resp['result']['practopbanad']['adtype'] == 'html5':
        setHtml('jiaxiao.html', 'html', resp['result']['practopbanad']['data'][0]['html'])
      elif resp['result']['practopbanad']['adtype'] == 'native':
        setHtml('jiaxiao.html', 'img', resp['result']['practopbanad']['data'][0]['imageurl'])

    time.sleep(2)
    url = jiaxiaoHeader + str(getCurrentTime()) + jiaxiaoEnd
  except Exception as e:
    print('出现异常==>', e)
    # 重新请求
    time.sleep(100)
    getJiaxiaoAd()
  except AttributeError as e:
    print("Tag was not found")


def main():
  for x in range(100):
    if GL.jiaxiaoCount != 0 and GL.jiaxiaoCount % 3 == 0:
      os.system('taskkill  /F /IM firefox.exe')

    getBiduVideoAd()
    getFitAd()
    getHangjiashuoAd()
    getJiaxiaoAd()


if __name__ == '__main__':
  main()

# -*-coding:utf-8 -*-
# 百度视频
import requests
import time
import json
import webbrowser
from requests import HTTPError

# 请求的时间戳
currentTime = int(time.time())

urlHeader = 'http://app.video.baidu.com/adver/?terminal=adnative&adver_version=0.0.0&position=stop&works_id=short_video_e451c7d7c5a7118c65a725a8753324c9&site=http%3A%2F%2Fbaishi.baidu.com%2Fwatch%2F7788471627219284212.html&online=1&video_type=normal&play_channel=&block_sign=amuse&dpi=320&player_style=card&device=android&os=1&os_version=23&screen_width=720&screen_height=1280&imei=866117035052641&locale=zh_CN&vendor=vivo&model=vivo+Y66&android_id=d70ac4e6752e71f9&connection_type=100&operator_type=0&orientation=p&uniqueid=2b60c2a37c60dbfd6626f617b5d78779&mtj_cuid=5E9A7E636F8C5565B2281683B66E45C4%7C146250530711668&mtj_timestamp=1559299005956&mac_address=02:00:00:00:00:00&ados_ver=6.0.1&dev=vivoY66&lf=eyJsb25naXR1ZGUiOiIxMTYuMzU1NjIiLCJsYXRpdHVkZSI6IjM5Ljk4MTc3In0%3D%0A&channel=563o&version=8.10.1&_smc=0&_irt=0&_adsdk=23&fstapktime='
url = urlHeader + str(currentTime)
html = ''
for x in range(10):
  try:
    res = requests.get(url, verify=False)
    print('第' + str(x) + '次获取广告数据 ===========>')
    print('状态码==>', res.status_code)
    print('报文头==>', res.headers)
    print('body ==>', res.text)
    resp = json.loads(res.text)

    requests.get(resp['reqtime'])
    requests.get(resp['data']['stop'][1]['data'][0]['request'])

    # for i in range(len(resp['data']['stop'][1]['data'][0]['thirdparty_url'])):
    #   if resp['data']['stop'][1]['data'][0]['thirdparty_url'][i] != '':
    #     requests.get(resp['data']['stop'][1]['data'][0]['thirdparty_url'][i])

    if resp['data']['stop'][1]['category'] == 'dsp':
      # 命名生成的html
      GEN_HTML = "baiduVideo.html"
      f = open(GEN_HTML, 'w')
      html = """
               <html>
               <head></head>
               <body>
               <img src=%s>
               </body>
               </html>""" % (resp['data']['stop'][1]['data'][0]['multi_img'][0])
      f.write(html)
      f.close()
      # 运行完自动在网页中显示
      webbrowser.open(GEN_HTML, new=0, autoraise=True)


    # 重新赋值
    time.sleep(10)
    currentTime = int(time.time())
    url = urlHeader + str(currentTime)
  except HTTPError as e:
    print('出现异常==>', e)
  except AttributeError as e:
    print("Tag was not found")

import os
import pyjadx
import signal
import subprocess
import warnings
import xml.dom.minidom
from typing import Callable
import zipfile

jadx = pyjadx.Jadx()

# 解析apk包
try:
  app = jadx.load("zhihu_1192.apk")
  # 遍历查找对应类名
  for cls in app.classes:
    if ("MobSDK" in cls.fullname):
      print("Mob SDK====> " + cls.fullname)
    if ("UMConfigure" in cls.fullname):
      print("Umeng SDK====> " + cls.fullname)
    if ("JAnalyticsInterface" in cls.fullname):
      print("JAnalytics SDK====> " + cls.fullname)
    if ("com.igexin.sdk.PushService" in cls.fullname):
      print("getui SDK====> " + cls.fullname)
    if ("TCAgent" in cls.fullname):
      print("TalckingData SDK====> " + cls.fullname)
except Exception as e:
  print("出现异常情况====> ", e)


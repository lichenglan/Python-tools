
from appium import  webdriver

caps = {}

caps['platformName'] = 'Android'
caps['platformVersion'] = '7.1.1'
caps['deviceName'] = 'ZX1G225RRF'
caps['appPackage'] = 'com.moji.mjweather'
caps['appActivity'] = 'com.moji.mjweather.MainActivity'
#隐藏键盘
caps['unicodeKeyboard'] = True
caps['resetKeyboard'] = True
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)

driver.swipe()
# if __name__ == '__main__':
#
#     pass
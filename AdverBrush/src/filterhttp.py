import mitmproxy.http
from mitmproxy import ctx


class Counter:
  def __init__(self):
    self.num = 0

  def request(self, flow: mitmproxy.http.HTTPFlow):
    ctx.log.info("flow.request.url" % flow.request.url)
    ctx.log.info("flow.request.host" % flow.request.host)
    if "ad.api.moji.com" in flow.request.url or "cdn.shuzijz.cn" in flow.request.url:
      self.num = self.num + 1

    ctx.log.info("We've seen %d flows" % self.num)


# mitmproxy -p 6666 -filter.py

addons = [
  Counter()
]

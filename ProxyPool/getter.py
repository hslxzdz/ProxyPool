from storage import RedisClient
from crawler import Crawler
from setting import MAX_POOL_COUNT

class Getter():
    def __init__(self):
        self.db = RedisClient()
        self.crawler = Crawler()

    def is_over_threshold(self):
        """
        是否超出代理池限制
        """
        if self.db.count() > MAX_POOL_COUNT:
            return True
        else:
            return False

    def run(self):
        """
        :return:
        """
        print('start to get proxy')
        if not self.is_over_threshold():
            for item in range(self.crawler.__CrawlFuncCount__):
                callback = self.crawler.__CrawlFunc__[item]
                proxies = self.crawler.get_proxy(callback)
                for proxy in proxies:
                    self.db.add(proxy)
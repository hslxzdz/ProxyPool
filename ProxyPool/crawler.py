from pyquery import PyQuery as pq
from utils import get_page
import requests
import time

class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k,v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count+=1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls,name,bases,attrs)

class Crawler(object, metaclass=ProxyMetaclass):
    def get_proxy(self, callback):
        proxies = []
        for proxy in eval('self.{}()'.format(callback)):
            print('成功获取到代理',proxy)
            proxies.append(proxy)
        return proxies

    def crawl_daili66(self, page_count=4):
        url = 'http://www.66ip.cn/{}.html'
        for i in range(1,page_count+1):
            target_url=url.format(i)
            content = pq(get_page(target_url))
            content = content('.containerbox table tr:gt(0)').items()
            for item in content:
                ip = item.find('td:nth-child(1)').text()
                port = item.find('td:nth-child(2)').text()
                yield ':'.join([ip, port])

    def crawl_ip3366(self, page_count=4):
        url = 'http://www.ip3366.net/free/?stype=1&page={}'
        for i in range(1,page_count+1):
            target_url = url.format(i)
            content = pq(get_page(target_url))
            content = content('.table-striped tbody tr').items()
            for item in content:
                ip = item('td:nth-child(1)').text()
                port = item('td:nth-child(2)').text()
                yield ':'.join([ip,port])

    def crawl_kuaidaili(self, page_count=4):
        url = 'https://www.kuaidaili.com/free/inha/{}/'
        for i in range(1,page_count+1):
            target_url = url.format(i)
            content = pq(get_page(target_url))
            content = content('.table-striped tbody tr').items()
            for item in content:
                ip = item('td:nth-child(1)').text()
                port = item('td:nth-child(2)').text()
                yield ':'.join([ip,port])
            time.sleep(1)#该网站有访问频率限制

    def crawl_xicidaili(self, page_count=4):
        url = 'http://www.xicidaili.com/nn/{}'
        for i in range(1,page_count+1):
            target_url=url.format(i)
            content = pq(get_page(target_url))
            content = content('table tr:gt(0)').items()
            for item in content:
                ip = item('td:nth-child(2)').text()
                port = item('td:nth-child(3)').text()
                yield ':'.join([ip,port])
if __name__=='__main__':
    for item in crawl_xicidaili():
        print(item)
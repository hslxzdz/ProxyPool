from storage import RedisClient
import requests
from setting import *
import asyncio
import aiohttp
import sys
import time

class Tester():
    def __init__(self):
        self.redis = RedisClient()

    async def test_single_proxy(self,proxy):
        conn = aiohttp.TCPConnector(verify_ssl=False)
        async with aiohttp.ClientSession(connector=conn) as session:
            try:
                if isinstance(proxy,bytes):
                    proxy = proxy.decode('utf-8')
                real_proxy = 'http://'+proxy
                print('正在测试',real_proxy)
                async with session.get(TEST_API,proxy=real_proxy,timeout=15,allow_redirects=False) as response:
                    if response.status in VALID_STATUS_CODE:
                        self.redis.enable(proxy)
                        print('代理 ',proxy,' 可用')
                    else:
                        self.redis.decrease(proxy)
                        print('代理 ',proxy,' 请求失败')
            except:
                self.redis.decrease(proxy)
                print('代理 ' ,proxy, ' 不可用')
    def run(self):
        print('开始测试')
        try:
            for i in range(0,self.redis.count(),BATCH_TEST_COUNT):
                start = i
                end = min(i+BATCH_TEST_COUNT,self.redis.count())
                proxies = self.redis.batch(start,end)
                print('正在测试第 ',start,'到',end,'个代理')
                tasks = [self.test_single_proxy(proxy) for proxy in proxies]
                loop = asyncio.get_event_loop()
                loop.run_until_complete(asyncio.wait(tasks))
                sys.stdout.flush()
                time.sleep(5)
        except Exception as e:
            print('测试错误 ', e.args)


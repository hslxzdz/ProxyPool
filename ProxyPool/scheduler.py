from multiprocessing import Process
from storage import RedisClient
from getter import Getter
from tester import Tester
from api import app
from setting import *
import time

class Scheduler():
    def scheduler_tester(self,cycle=TEST_CYCLE):
        test = Tester()
        while True:
            print('开始测试代理')
            test.run()
            time.sleep(cycle)
    def scheduler_getter(self,cycle=GET_CYCLE):
        getter = Getter()
        while True:
            print('开始抓取代理')
            getter.run()
            time.sleep(cycle)
    def scheduler_api(self):
        # app.run(GET_HOST,GET_PORT)
        app.run()
    def run(self):
        print('代理池开始运行')
        if GETTER_ENABLED:
            getter_process = Process(target=self.scheduler_getter)
            getter_process.start()
        if TESTER_ENABLED:
            tester_process = Process(target=self.scheduler_tester)
            tester_process.start()
        if API_ENABLED:
            api_process = Process(target=self.scheduler_api)
            api_process.start()
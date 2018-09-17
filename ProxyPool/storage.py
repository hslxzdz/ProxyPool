import redis
from setting import REDIS_HOST, REDIS_PORT, PASSWORD, \
    REDIS_KEY, MAX_SCORE, MIN_SCORE, INITIAL_SCORE
from random import choice

class RedisClient():
    def __init__(self,host=REDIS_HOST, port=REDIS_PORT, password=PASSWORD):
        """
        :param REDIS_HOST: 地址
        :param REDIS_PORT: 端口
        :param PASSWORD: 密码
        """
        self.db = redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT,db=0,password=PASSWORD)

    def add(self,proxy,score=INITIAL_SCORE):
        """
        :param proxy: 代理
        :param INITIAL_SCORE: 初始分数
        :return: 添加结果
        """
        if not self.db.zscore(REDIS_KEY,proxy):
           return self.db.zadd(REDIS_KEY,score,proxy)

    def decrease(self,proxy):
        """
        :param proxy:
        :return: 减分结果
        """
        score = self.db.zscore(REDIS_KEY,proxy)
        if score and score>MIN_SCORE:
            print('代理 ',proxy,' score ',score,' 减1')
            return self.db.zincrby(REDIS_KEY, proxy, -1)
        else:
            print('代理 ',proxy,' 移除')
            return self.db.zrem(REDIS_KEY,proxy)
    def enable(self,proxy):
        """
        :param proxy:
        :return: 插入结果
        """
        score = self.db.zscore(REDIS_KEY,proxy)
        if score:
            print('代理 ',proxy,' 可用 score 100')
            return self.db.zadd(REDIS_KEY,MAX_SCORE,proxy)

    def random(self):
        """
        :return: 随机取出一个结果
        """
        result = self.db.zrangebyscore(REDIS_KEY,MAX_SCORE,MAX_SCORE)
        if not result:
            result = self.db.zrevrange(REDIS_KEY,0,100)
            if not result:
                print('ProxyEmptyError')
        return choice(result)

    def count(self):
        """
        :return: 代理池数量
        """
        return self.db.zcard(REDIS_KEY)

    def exist(self,proxy):
        """
        :return: 是否存在
        """
        return not self.db.zscore(REDIS_KEY,proxy)==None

    def all(self):
        """
        :return: 所有代理
        """
        return self.db.zrangebyscore(REDIS_KEY,MIN_SCORE,MAX_SCORE)

    def batch(self,start,stop):
        """
        :return: 代理列表
        """
        return self.db.zrevrange(REDIS_KEY,start,stop)

if __name__=='__main__':
    conn = RedisClient()
    result = conn.batch(680,688)
    print(result)
#Redis数据库地址
REDIS_HOST = '127.0.0.1'

#Redis数据库端口
REDIS_PORT = '6379'

#Redis密码
PASSWORD = None

#REDIS_KEY
REDIS_KEY = 'proxy'

#代理分数
MAX_SCORE = 100
MIN_SCORE = 1
INITIAL_SCORE = 10

#状态码
VALID_STATUS_CODE = [200,302]

#代理池上限
MAX_POOL_COUNT = 50000

#检测周期
TEST_CYCLE = 20

#获取周期
GET_CYCLE = 300

#测试api
TEST_API = 'http://www.baidu.com'

#获取api
GET_HOST = '0.0.0.0'
GET_PORT = '5555'

#开关
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True

#最大批测试量
BATCH_TEST_COUNT = 100

import requests
from requests.exceptions import ConnectionError
base_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
}
def get_page(url,options={}):
    headers = dict(base_headers,**options)
    try:
        result = requests.get(url,headers=headers)
        if result.status_code==200:
            text = result.text
            return text
    except ConnectionError:
        print('抓取失败',url)
        return None
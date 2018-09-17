from flask import Flask, g
from storage import RedisClient

__all__ = ['app']

app = Flask(__name__)

def conn():
    if not hasattr(g, 'conn'):
        g.conn = RedisClient()
        return g.conn
@app.route('/')
def index():
    return 'welcome'

@app.route('/proxy')
def get_proxy():
    return conn().random()

@app.route('/count')
def get_count():
    return str(conn().count())

if __name__ == '__main__':
    app.run()
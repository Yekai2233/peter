from flask import Flask
from redis import Redis
import time

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    with open('./log/ll.log') as f:
        f.write('{}-{}'.format(str(count), str(time.time())))
    return 'Hello World! 该页面已被访问 {} 次。\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

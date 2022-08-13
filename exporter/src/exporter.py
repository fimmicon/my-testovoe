from prometheus_client import start_http_server
from prometheus_client import Histogram, Counter, Gauge
import random, time

PUBLISH_PERIOD=0.1 # Interval for updating metrics


c = Counter('number_of_requests', 'The number of requests')

c2 = Counter('my_requests_total', 'HTTP Requests', ['method', 'endpoint'])
endpoints = ("/main", "/contacts", "/about", "/cart", "/catalog")
methods = ("GET", "PATCH", "POST")

g = Gauge('system_usage', 'Hold current system resource usage', ['resource_type' ,'server_name'])

h = Histogram('uploaded_image_bytes', 'Size of uploaded image file', buckets=[ 64, 256, 1024, 4096, 16384, 16384, 262144, 1048576, 4194304, 16777216 ] )

if __name__ == '__main__':
    start_http_server(8000)
    while True:
        c.inc(random.randint(0, 1))

        c2.labels(random.choice(methods), random.choice(endpoints)).inc()        

        g.labels('CPU', 'webserver').set(random.randint(0,100))
        g.labels('Memory', 'webserver').set(random.randint(0,50))

        g.labels('CPU', 'dbserver').set(random.randint(0,50))
        g.labels('Memory', 'dbserver').set(random.randint(0,100))

        h.observe(random.randint(3, 16800000))

        time.sleep(PUBLISH_PERIOD)

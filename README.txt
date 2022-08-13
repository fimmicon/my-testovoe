Launch, using: ./run.sh
After launch, wait 1-2min to scrape some metrics.

Required: docker and docker-compose installed on your machine
          and ports 8000, 9090, 3000 should be available

Here I write 127.0.0.1, but you can access endpoint using other ip addresses on your interfaces.

Endpoints:
exporter:    http://127.0.0.1:8000/
prometheus:  http://127.0.0.1:9090
grafana:     http://127.0.0.1:3000

You can go to dashboards and look without signing in grafana.
             http://127.0.0.1:3000/d/example/example-dashboard
(If you want Sign In grafana, use admin:admin)


Do not forget to shut down and cleanup, using: docker-compose down -v --rmi all

==============================================================================

exporter ( ./exporter/src/exporter.py )

Exposed metrics:

Counter (c and c2 objects) - used in Dashboards "Total requests per minute" and "HTTP Requested Urls".
Gauge (g object) - used in Dashboards "Memory Usage" and "CPU Usage", with different labels.
Histogram (h object) - used in Dashboards "Files smaller than 4MB" and "Files bigger than 4MB".

All exposed metrics are dummy and generated randomly.

==============================================================================
Grafana (./grafana/)

JSON file for dashboard located in ./grafana/dashboards/example.json

Used Links:
https://github.com/prometheus/client_python
https://github.com/rycus86/prometheus_flask_exporter/tree/master/examples/sample-signals
https://gist.github.com/sysdig-blog/22ef4c07714b1a34fe20dac11a80c4e2
https://github.com/slok/prometheus-python/blob/master/examples/memory_cpu_usage_example.py
https://github.com/jonashaag/prometheus-multiprocessing-example
https://github.com/amitsaha/python-prometheus-demo/tree/master/flask_app_prometheus
https://grafana.com/blog/2020/06/23/how-to-visualize-prometheus-histograms-in-grafana/

https://pub.dev/documentation/prometheus_client/latest/prometheus_client/Histogram-class.html

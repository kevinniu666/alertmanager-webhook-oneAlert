# coding=UTF-8
import  requests
# content = {
#  "app": "5913da62-69b0-ac5a-d0ed-a591e05f800c",
#  "eventId": "3458867",
#  "eventType": "trigger",
#  "alarmName": "sent from API",
#  "entityName": "host-192.168.0.253",
#  "entityId": "host-192.168.0.253",
#  "priority": 1,
#  "alarmContent": {
#  "ping time": "1500ms",
#  "load avg": 0.75},
#  "details": {
#    "details":"发送自API"
#  },
#  "contexts": [
#  {
#     "type": "link",
#     "text": "generatorURL",
#     "href": "http://www.baidu.com"
#  },
#  {
#     "type": "link",
#     "href": "http://www.sina.com",
#     "text": "CPU Alerting"
#  },
#  {
#     "type": "image",
#     "src": "http://www.baidu.com/a.png"
#  }]
#  }
content={
  "status": "resolved",
  "groupLabels": {},
  "groupKey": "{}:{}",
  "commonAnnotations": {
    "description": "Test Prometheus / isn't working."
  },
  "alerts": [
    {
      "status": "firing",
      "labels": {
        "prometheus": "monitoring/k8s",
        "severity": "warning",
        "alertname": "ExampleAlert"
      },
      "endsAt": "0001-01-01T00:00:00Z",
      "generatorURL": "http://prometheus-k8s-0:9090/graph?g0.expr=vector%281%29&g0.tab=1",
      "startsAt": "2019-03-01T02:16:55.528170792Z",
      "annotations": {
        "description": "Test Prometheus / isn't working."
      }
    }
  ],
  "version": "4",
  "receiver": "onealert",
  "externalURL": "http://alertmanager-main-0:9093",
  "commonLabels": {
    "prometheus": "monitoring/k8s",
    "severity": "warning",
    "alertname": "ExampleAlert"
  }
}
resolved = {
  "status": "resolved",
  "groupLabels": {},
  "groupKey": "{}:{}",
  "commonAnnotations": {
    "description": "Test Prometheus / isn't working."
  },
  "alerts": [
    {
      "status": "resolved",
      "labels": {
        "prometheus": "monitoring/k8s",
        "severity": "warning",
        "alertname": "ExampleAlert"
      },
      "endsAt": "2019-03-01T03:01:55.528170792Z",
      "generatorURL": "http://prometheus-k8s-1:9090/graph?g0.expr=vector%280%29&g0.tab=1",
      "startsAt": "2019-03-01T02:16:55.528170792Z",
      "annotations": {
        "description": "Test Prometheus / isn't working."
      }
    }
  ],
  "version": "4",
  "receiver": "onealert",
  "externalURL": "http://alertmanager-main-0:9093",
  "commonLabels": {
    "prometheus": "monitoring/k8s",
    "severity": "warning",
    "alertname": "ExampleAlert"
  }
}

url = "http://api.onealert.com/alert/api/event"
headers = {'Content-Type': 'application/json;charset=UTF-8'}
#res = requests.request("post","http://192.168.1.106/",json=content,headers=headers)
# res = requests.request("post",url,json=content,headers=headers)
res=requests.post('http://192.168.1.106/',json=content)
print(res.status_code)
print(res.text)
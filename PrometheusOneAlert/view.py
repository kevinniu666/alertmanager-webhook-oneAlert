#coding=utf-8
from django.http import HttpResponse,JsonResponse
import json,simplejson,hashlib,os,requests
# import logging
def encrpyt_string(str):
    md = hashlib.md5()
    md.update(str.encode())
    encrpted_str = md.hexdigest()
    # print encrpted_str
    return encrpted_str
def hello(request):
    return HttpResponse("Hello world ! ")
def send_alert_to_prometheus(request):
    data = json.loads(request.body)
    print json.dumps(data, indent=2)
    print data
    return HttpResponse('OK')
def send_alert(request):
    oneAlertAPI = "http://api.onealert.com/alert/api/event"
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    data = json.loads(request.body)
    # app = os.getenv('ApplicationKey')
    app = '5913da62-69b0-ac5a-d0ed-a591e05f800c'
    print type(data['alerts'][0]['startsAt'])
    md5_key = str(data['alerts'][0]['startsAt']) + str(data['alerts'][0]['labels']['alertname'])
    print str(md5_key)
    eventId = str(encrpyt_string(md5_key))
    print type(eventId)
    print 'eventId is:\n' + eventId + "\n"
    if data['status'] == 'firing':
        eventType = 'trigger'
    else:
        eventType = 'resolve'

    #eventType = ''
    alarmName = str(data['alerts'][0]['labels']['alertname'])
    entityName = 'PlaceHolder'
    entityId = 'PlaceHolder'
    priority = ''
    if data['alerts'][0]['labels']['severity'] == 'warning':
        priority = '2'
    elif data['alerts'][0]['labels']['severity'] == 'info':
        priority = '1'
    else:
        priority = '3'
    alarmContent = str(data['alerts'][0]['annotations'])
    details = data['alerts'][0]
    contexts = data['alerts']

    content = {
        "app": app,
        "eventId": eventId,
        "eventType": eventType,
        "alarmName": alarmName,
        "entityName": entityName,
        "entityId": entityId,
        "priority": priority,
        "alarmContent": alarmContent,
        "details": details,
        "contexts": contexts
    }
    print '-------------Data Send to oneAlert-----------\n'
    print json.dumps(content, indent=2)
    res = requests.request("post",oneAlertAPI,json=content,headers=headers)
    print '-------------Response from oneAlert----------\n'
    print(res.status_code)
    print(res.text)
    return JsonResponse(res.text,safe=False)
    # for key,value in data.items():
    #     print key,value
    #print json.dumps(data,indent=2)
    # contexts={
    #     "receiver": "onealert",
    #     "status": "firing",
    #     "alerts": [{
    #         "status": "firing",
    #         "labels": {
    #             "alertname": "ExampleAlert",
    #             "prometheus": "monitoring/k8s"
    #         },
    #         "annotations": {},
    #         "startsAt": "2019-02-28T08:21:37.99174658Z",
    #         "endsAt": "0001-01-01T00:00:00Z",
    #         "generatorURL ": "http: //prometheus-k8s-0:9090/graph?g0.expr=vector%281%29\u0026g0.tab=1"
    #     }],
    #     "groupLabels": {},
    #     "commonLabels": {
    #         "alertname": "ExampleAlert",
    #         "prometheus": "monitoring/k8s"
    #     },
    #     "commonAnnotations": {},
    #     "externalURL": "http://alertmanager - main - 0: 9093 ",
    #     "version ": "4 ",
    #     "groupKey ": " {}: {}"
    # }
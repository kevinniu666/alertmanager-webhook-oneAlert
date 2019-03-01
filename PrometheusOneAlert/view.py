#coding=utf-8
from django.http import HttpResponse,JsonResponse
import json,simplejson,hashlib,os,requests
# import logging
def encrpyt_string(str):
    md = hashlib.md5()
    md.update(str.encode())
    encrpted_str = md.hexdigest()
    return encrpted_str
def send_alert(request):
    oneAlertAPI = "http://api.onealert.com/alert/api/event"
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    data = json.loads(request.body)
    app = os.environ['APPLICATION_KEY']
    # app = '5913da62-69b0-ac5a-d0ed-a591e05f800c'
    md5_key = str(data['alerts'][0]['startsAt']) + str(data['alerts'][0]['labels']['alertname'])
    eventId = str(encrpyt_string(md5_key))
    if data['status'] == 'firing':
        eventType = 'trigger'
    else:
        eventType = 'resolve'
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
    if len(str(app)) != 0:
       res = requests.request("post",oneAlertAPI,json=content,headers=headers)
    else:
       print "oneAlert ApplicationKey is null!"
    print '-------------Response from oneAlert----------\n'
    print(res.text)
    return JsonResponse(res.text,safe=False)
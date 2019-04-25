#coding=utf-8
from django.http import HttpResponse
import os,requests

def send_alert(request):
    phoneCallUrl = "http://ops.dadingsoft.com/voice"
    phoneCallToken = os.environ['PHONECALL_TOKEN']
    #phoneCallToken = 'wJ4S4iysHZKQKWzWYd9b'
    res=requests.get(phoneCallUrl,{'token': phoneCallToken})
    print(res.text)
    if res.json()["status"] == 'ok':
        return HttpResponse("sucess")
    else:
        return  HttpResponse("failed")
def healthz(request):
    return HttpResponse("success")
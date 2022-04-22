import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import AccountingRecord, AccountingMember, AccountingType

from linebot.exceptions import InvalidSignatureError, LineBotApiError

from messagebot.event_handle import handler

def hello(request):
    return HttpResponse('hello world')

def record_create(msg):
    #自己 午餐 100 4/21 <註記>
    member = AccountingMember.objects.filter(name=msg[0]).first()
    accounting_type = AccountingType.objects.filter(name=msg[1]).first()
    cost = int(msg[2])
    month, day = msg[3].split('/')
    date = datetime.date(datetime.datetime.now().date().year, int(month), int(day))
    note = None if len(msg) < 5 else msg[4]

    record = AccountingRecord.objects.create(member_id=member, accounting_type_id=accounting_type, cost=cost,
                                             date=date, note=note)
    record.save()




@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            print('Invalid signature. Please check your channel access token/channel secret.')
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        return HttpResponse()
    else:
        return HttpResponseBadRequest()


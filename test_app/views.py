from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
import string
import random

# Create your views here.


def hello(request):
    return HttpResponse('hello')


def gen_password(request):
    try:
        if int(request.GET.get('param1')) <= 0:
            return HttpResponse('param1 must be >0')
        else:
            if int(request.GET.get('param1')) <8 or int(request.GET.get('param1')) > 24:
                return HttpResponse('param1 must be between 8 and 24')
            else:
                if request.GET.get('param2') == 'yes':
                    return HttpResponse(''.join([
                        random.choice(string.ascii_lowercase + string.digits)
                        for _ in range(int(request.GET.get('param1')))
                    ]))
                elif request.GET.get('param2') == 'no':
                    return HttpResponse(''.join([
                        random.choice(string.ascii_lowercase)
                        for _ in range(int(request.GET.get('param1')))
                    ]))
    except ValueError:
        return HttpResponse('Param1 must be a number')


def get_customers(request):
    print(request.GET)
    query = f'select * from customers where State = "{request.GET.get("state")}" and City = "{request.GET.get("city")}"'
    records = execute_query(query)
    return HttpResponse(records)


def execute_query(query):
    db_path = '/home/dmitry/Downloads/Telegram Desktop/chinook.db'
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(query)
    records = cur.fetchall()
    return records


def get_unique_name(request):
    query = 'select distinct FirstName from customers'
    records = execute_query(query)
    num = 0
    for _ in records:
        num += 1
    return HttpResponse(f'{num}')


def get_value(request):
    q = 'select UnitPrice * Quantity from invoice_items'
    rec = execute_query(q)
    return HttpResponse(f'{rec}')


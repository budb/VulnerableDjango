from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
import sqlite3


def hello(request):
    return HttpResponse("Hello world")


def stage_1(request):
    return render_to_response('index.html')

def stage_2(request):
	return render_to_response('login.html')

def stage_3(request):
    return render_to_response('welcome.html')


@csrf_exempt
def pass_1(request):
    if request.method == "POST":
        get_text = request.POST["password"]
    if get_text == "batman":
        return render_to_response('login.html')
    else:
        return render_to_response('index.html')

@csrf_exempt
def pass_2(request):
    conn = sqlite3.connect("userdata.db")
    c = conn.cursor()


    if request.method == "GET":
        username = request.GET["username"]
        password = request.GET["password"]

        c.execute("SELECT * FROM USER WHERE username='{0}'" .format(username))
        data = c.fetchone()
        
    if data is None:
        return render_to_response('login.html')
    else:
        c.execute("SELECT password FROM USER WHERE username='{0}'" .format(username))
        data = c.fetchone()

    if password == data[0]:
        return render_to_response('welcome.html')
        
    else:
        return render_to_response('login.html')



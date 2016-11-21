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
    return render_to_response('login2.html')

def stage_4(request):
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

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        makeMeInjectable = "SELECT password FROM USER WHERE username='%s'" %(username,)
        c.execute(makeMeInjectable)
        data = c.fetchone()

    if data is None:
        return render_to_response('login2.html')
    elif password == data[0]:
        return render_to_response('welcome.html')       
    else:
        return render_to_response('login2.html')

@csrf_exempt
def pass_3(request):
    conn = sqlite3.connect("userdata.db")
    c = conn.cursor()

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        veryVulnerable = "SELECT password FROM USER WHERE username='%s'" %(username,)
        c.execute(veryVulnerable)
        data = c.fetchone()
    
    if data is None:
        return render_to_response('login2.html')
    elif password == data[0]:
        return render_to_response('welcome.html')
    else:
        return render_to_response('login2.html')
        



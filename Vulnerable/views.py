import sys, os
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
import sqlite3, logging

logger = logging.getLogger(__name__)

@csrf_exempt
def stage_1(request):
    if request.method == "GET":
        return render_to_response('index.html')
    elif request.method == "POST":
        get_text = request.POST["password"]
        if get_text == "batman":
            return render_to_response('login.html')
        else:
            return render_to_response('index.html')

@csrf_exempt
def stage_2(request):
    if request.method == "GET":
        return render_to_response('login.html')
    elif request.method == "POST":
        conn = sqlite3.connect("userdata.db")
        c = conn.cursor()

        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            makeMeInjectable = "SELECT password FROM USER WHERE username='%s'" % (username,)
            c.execute(makeMeInjectable)
            data = c.fetchone()

        if data is None:
            return render_to_response('login2.html')
        elif password == data[0]:
            return render_to_response('welcome.html')
        else:
            return render_to_response('login2.html')

@csrf_exempt
def stage_3(request):
    if request.method == "GET":
        return render_to_response('login2.html')
    elif request.method == "POST":
        conn = sqlite3.connect("userdata.db")
        c = conn.cursor()

        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]

            veryVulnerable = "SELECT password FROM USER WHERE username='%s'" % (username,)
            c.execute(veryVulnerable)
            data = c.fetchone()

        if data is None:
            return render_to_response('login2.html')
        elif password == data[0]:
            return render_to_response('welcome.html')
        else:
            return render_to_response('login2.html')

@csrf_exempt
def stage_4(request):
    if request.method == "GET":
        return render_to_response('welcome.html')
    elif request.method == "POST":
        action = request.POST["action"]
        logger.debug(action)
        os.system(action)
        return render_to_response('welcome.html')




        



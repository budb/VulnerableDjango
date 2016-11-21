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
        return render_to_response('stage_1.html')
    elif request.method == "POST":
        get_text = request.POST["password"]
        if get_text == "batman":
            return render_to_response('stage_2.html')
        else:
            return render_to_response('stage_1.html')

@csrf_exempt
def stage_2(request):
    if request.method == "GET":
        return render_to_response('stage_2.html')
    elif request.method == "POST":
        conn = sqlite3.connect("userdata.db")
        c = conn.cursor()

        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            makeMeInjectable = "SELECT id FROM USER WHERE username='%s' and password='%s'" % (username, password,)
            c.execute(makeMeInjectable)
            data = c.fetchone()

        if data is None:
            return render_to_response('stage_2_error.html')
        else:
            return render_to_response('stage_3.html')

@csrf_exempt
def stage_3(request):
    if request.method == "GET":
        return render_to_response('stage_3.html')
    elif request.method == "POST":
        action = request.POST["action"]
        logger.debug(action)
        os.system(action)
        return render_to_response('stage_3.html')


        



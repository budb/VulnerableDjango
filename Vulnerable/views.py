import threading, subprocess as sub
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, render
import sqlite3, logging

logger = logging.getLogger(__name__)


def stage_1(request):
    if request.method == "GET":
        return render(request, 'stage_1.html')
    elif request.method == "POST":
        get_text = request.POST["password"]
        if get_text == "batman":
            return render(request, 'stage_2.html')
        else:
            return render(request, 'stage_1.html')


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
        t = threading.Thread(target=worker, args=(action,))
        t.daemon = True
        t.start()
        return render_to_response('stage_3.html')


def worker(action):
    print('Worker: %s' % action)
    p = sub.Popen([action], shell=True, stderr=sub.STDOUT, stdout=sub.PIPE)
    output, errors = p.communicate()
    print('Action: %s' % output)
    return


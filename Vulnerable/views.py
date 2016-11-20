from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt


def hello(request):
    return HttpResponse("Hello world")


def stage_1(request):
    return render_to_response('index.html')


@csrf_exempt
def pass_1(request):
    if request.method == "POST":
        get_text = request.POST["password"]
    if get_text == "batman":
        return HttpResponse("test")
    else:
        return render_to_response('index.html')



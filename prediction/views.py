from django.shortcuts import render
from django.http import HttpResponse
# from django.http import JsonResponse
from PIL import Image
import os

send_pipe = "/tmp/gtImageStream.pipe"
recv_pipe = "/tmp/gtResultSteam.pipe"

try:
    # create named_pipe
    os.mkfifo(send_pipe)
    os.mkfifo(recv_pipe)
except OSError as err:
    print(err)


def index(request):
    print("access index")
    return HttpResponse("SUCC")


def init(request):
    # os.system("python3 gtPred.py")
    return HttpResponse("Initialized")


def upload(request):
    print("predict images")
    upload_file = request.FILES['file']

    img = Image.open(upload_file)
    img.save('/Users/GreysTone/Desktop/Dev/Porus_Server/uploaded/target.jpg')
    # img = img.convert('RGB')
    # img = img.resize(299, 299)

    send_port = os.open(send_pipe, os.O_CREAT | os.O_RDWR)

    os.write(send_port, bytes("trigger", 'utf-8'))
    recv_port = os.open(recv_pipe, os.O_RDONLY)
    result = os.read(recv_port, 1024)
    os.close(send_port)
    os.close(recv_port)

    # print(image.name)
    # file_path = '/Users/GreysTone/Desktop/Dev/Porus_Server/uploaded/target.jpg'
    # img.save(file_path)

    # prediction progress
    # result = gtPredict.predImg(model, img)

    # return JsonResponse(result)
    print(result)
    return HttpResponse(result)



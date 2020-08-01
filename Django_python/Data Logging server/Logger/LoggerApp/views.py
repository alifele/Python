from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
import matplotlib.pyplot as plt


# Create your views here.
@csrf_exempt
def hello(request):
    if request.method == "POST":
        #myfile = request.FILES['file'].read()
        #print(request.FILES['file'].read())
        if request.FILES:
            print(request.FILES['file'])
            handle_uploaded_file(request.FILES['file'])
            print('ok')
            return HttpResponse('Ok')
        #plt.imsave('tt.jpg',)
        else:
            print(request.read())
            return HttpResponse('Ok')
    #print(request.method)
    else:
        return render(request, 'LoggerApp/index.html')


def handle_uploaded_file(f):
    with open(f'{f}', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

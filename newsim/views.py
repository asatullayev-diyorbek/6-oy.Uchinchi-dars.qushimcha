from django.shortcuts import render


def index1(request):
    return render(request, 'index.html')


def index2(request):
    return render(request, 'index-02.html')


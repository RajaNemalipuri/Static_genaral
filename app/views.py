from django.shortcuts import render

# Create your views here.
def insertimg(request):
    return render(request,'inserimage.html')


def hai(request):
    return render(request,'h1.html')

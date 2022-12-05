from django.shortcuts import render

# Create your views here.

def image_add(request):
    return render(request,'image_add.html')
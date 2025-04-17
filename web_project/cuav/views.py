from django.shortcuts import render
from django.http import HttpResponse
from .models import Vendor 
import cuav.custom_query




# Create your views here.



def home(request):
    return HttpResponse("CUAV main page!")

def index(request):
    return render(request,'cuav/hello.html')

def display_vendors(request):
    vendors = Vendor.objects.using("cuav")
    return render(request, 'cuav/display_vendors.html', {'vendors': vendors})


def display_device_count(request):
    ret_device_count = cuav.custom_query.Custom_sql().device_count
    return render(request, 'cuav/display_device_count.html', {'devices': ret_device_count})





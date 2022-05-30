from django.shortcuts import render
from django.http import HttpResponse


def base_response(station_list):

    return HttpResponse('안녕')



def first(request):
    return render(request, 'my_test.html')


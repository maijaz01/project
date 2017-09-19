from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def indexViews(request):
    import ipdb;ipdb.set_trace()
    return render(request, 'index.html')

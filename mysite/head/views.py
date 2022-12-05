from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    data = {
        "title": 'Main',
        'values':['some','hellow','123'],
        'obj': {
            'car': 'BMW',
            'years': '18',
            'hobby': 'Footboll'
        }
    }
    return render(request, 'head/index.html', data)

def about(request):
    return render(request, 'head/about.html')

def contacts(request):
    return render(request, 'head/contacts.html')
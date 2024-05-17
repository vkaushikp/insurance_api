from django.shortcuts import render

# Create your views here.
def home(request):
    return 'Hello world'

def get_plans(request):
    if request.method == 'post':
        pass
    return 'Hello world'

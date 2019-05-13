from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """
    Index page view
    """

    my_dict = {
        'title':"From your first Project week"
    }

    return render(request,'first_app/index.html',context=my_dict)

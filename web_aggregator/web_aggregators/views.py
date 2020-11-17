from django.shortcuts import render


# Create your views here.
def index(request):
    """ Hompage """
    return render(request, 'web_aggregators/index.html')

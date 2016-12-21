from django.shortcuts import render

from .models import kmeans,origin

# Create your views here.
def index(request):
    origin_list = origin.objects.all()
    context = {'origin_list': origin_list}
    return render(request, 'MateFinder/index.html', context)
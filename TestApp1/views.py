from django.shortcuts import render
from .models import task

def index(request):
    tasks = task.objects.all()
    if request.method == 'POST':
        a = request.POST.get('title')
        b = request.POST.get('description')
        task.objects.create(title=a, description=b)
    return render(request, 'home.html',{'tasks':tasks})

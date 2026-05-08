from django.shortcuts import render,redirect
from .models import task

def index(request):
    tasks = task.objects.all()
    if request.method == 'POST':
        a = request.POST.get('title')
        b = request.POST.get('description')
        task.objects.create(title=a, description=b)
    return render(request, 'home.html',{'tasks':tasks})

def delete(request, id):
    task.objects.filter(id=id).delete()
    return redirect('/')

def update(request, id):
    tasks = task.objects.filter(id=id).first()
    tasks.completed = not tasks.completed
    tasks.save()
    return redirect('/')
    
from django.shortcuts import render
from home.models import Task

# Create your views here.
def index(request):
    context={'success': False, 'name': 'Hancie Phago'}
    if request.method=='POST':
        title=request.POST['title']
        desc=request.POST['desc']
        ins= Task(title=title, desc=desc)
        ins.save()
        
        context={'success': True}


    return render(request, 'index.html', context)


def tasklist(request):
    allTask=Task.objects.all()
    context={'task': allTask}
    return render(request, 'tasklist.html', context)

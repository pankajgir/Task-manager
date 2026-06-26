from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import task

def task_list(request):
    Task=task.objects.all().order_by('-create_date')
    return render(request,'crdapp/task_list.html',{'task':Task})
def task_create(request):
    if request.method=='POST':
        title=request.POST.get('title','').strip()
        description=request.POST.get('descriptiion','').strip()
        if title:
            task.objects.create(title=title , descriptiion=description)
            return redirect(reverse('task-list'))
    return render(request,'crdapp/task_form.html')

def edit(request,pk):
    Task=get_object_or_404(task,pk=pk)
    if request.method=='POST':
        title=request.POST.get('title','').strip()
        description = request.POST.get('descriptiion', '').strip()
        completed=request.POST.get('completed')=='on'
        if title:
            Task.title=title
            Task.descriptiion=description
            Task.completed=completed
            Task.save()
            return redirect(reverse('task-list'))
        return render(request,'crdapp/task_form.html',{'task':Task,'error':'task can not be emty'})
    return render(request,'crdapp/task_form.html',{'task':Task})
    
def delete(request,pk):
    Task=get_object_or_404(task,pk=pk)
    if request.method=='POST':
        Task.delete()
        return redirect(reverse('task-list'))
    return render(request,'crdapp/task_confirm_delete.html',{'task':Task})


def task_toggle_completed(request,pk):
    Task=get_object_or_404(task,pk=pk)
    if request.method=="POST":
        Task.completed=not Task.completed
        Task.save()
    return redirect(reverse('task-list'))




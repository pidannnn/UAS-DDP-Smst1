from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.shortcuts import get_object_or_404

def home(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})

# Tambah tugas baru
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

# Edit tugas
def edit_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form})

# Hapus tugas
def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('home')

# Halaman untuk tugas yang sudah selesai
def completed_tasks(request):
    tasks = Task.objects.filter(completed=True)  # Ambil tugas yang sudah selesai
    return render(request, 'completed_tasks.html', {'tasks': tasks})

# Halaman untuk tugas yang belum selesai
def pending_tasks(request):
    tasks = Task.objects.filter(completed=False)  # Ambil tugas yang belum selesai
    return render(request, 'pending_tasks.html', {'tasks': tasks})
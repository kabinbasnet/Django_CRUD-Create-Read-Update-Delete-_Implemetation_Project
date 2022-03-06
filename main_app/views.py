from django.http import HttpResponse
from django.shortcuts import redirect, render
from main_app.models import TODO
# Create your views here.


def home(request):
    # storing all the database value on todo variable
    todo = TODO.objects.all()
    return render(request, 'main_app/home.html', {'todo': todo})


def add(request):
    if request.method == 'GET':
        return render(request, 'main_app/add.html')
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']

    # ::::::::::::::::::::::Adding its value on database table:::::::::::::::::::
    TODO.objects.create(title=title, content=content, is_complete=False)

    # 'redirect' is reverse url means that ==>> by using 'redirect' keyword it takes us from views to required url
    return redirect('home')


def edit(request, id):
    if request.method == 'GET':
        todo = TODO.objects.get(id=id)
        return render(request, 'main_app/edit.html', {'todo': todo})
    else:
        # title = request.POST['title']
        # content = request.POST['content']
        todo = TODO.objects.get(id=id)

        todo.title = request.POST['title']
        todo.content = request.POST['content']

        todo.save()  # It simply saves above value on 'todo' database table

        return redirect('home')


def delete(request, id):
    # todo.objects.get(id=id) means that ==>> we get the value of that 'id' from 'todo' database table
    todo = TODO.objects.get(id=id)
    todo.delete()  # todo.delete() means that ==>> deleting that id's required value from 'todo' database table

    return redirect('home')

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem,BinItem,DoneItem
from django.utils import timezone
from django.views.generic import ListView, CreateView
from todo.models import TodoItem,DoneItem,BinItem
from .forms import TodoModelForm

# def todoView(request):
#     all_todo_items = TodoItem.objects.all()
#     return render(request,'todo.html', {'all_items':all_todo_items})

class TodoList(ListView):
    # queryset = TodoItem.objects.all()
    # context_object_name ='all_items'
    model = TodoItem
    form_class = TodoModelForm
    paginate_by=10
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class TodoCreate(CreateView):
    model = TodoItem
    template_name = 'todo/todoitem_create.html'
    form_class = TodoModelForm
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)



def mybinView(request):
    mybin = BinItem.objects.all()
    print(mybin)
    return render(request,'mybin.html', {'all_items':mybin})

def mybinclearView(request):
    clear=BinItem.objects.all()
    clear.delete()
    return render(request,'mybin.html', )

def mydoneclearView(request):
    clear=DoneItem.objects.all()
    clear.delete()
    return render(request,'mydone.html', )


def mydoneView(request):
    mydone = DoneItem.objects.all()
    return render(request,'mydone.html',
    {'all_items':mydone})

def addTodo(request,):
    #取回post中的內容..
    if not  request.POST.get('deadline')  or not   request.POST.get('rating') or not request.POST.get('hours'):
        new_item = TodoItem(content=request.POST['content'])
    else:
        new_item = TodoItem(
            content = request.POST['content'],
            deadline = request.POST.get('deadline'),
            rating = request.POST.get('rating'),
            hours = request.POST.get('hours'),
        )
    new_item.save()
    return HttpResponseRedirect('/todo/')

def doneTodo(request,todo_id):
    item_to_done = TodoItem.objects.get(id=todo_id)
    a = DoneItem(id=item_to_done.id,
                            content=item_to_done.content,
                            done_time=timezone.now())
    a.save()
    item_to_done.delete()
    return HttpResponseRedirect('/todo/')


def deleteTodo(request,todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    a = BinItem(id=item_to_delete.id,
                            content=item_to_delete.content,
                            delete_time=timezone.now()
                            )

    a.save()
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')

def editTodo(request,todo_id):
    item_to_edit = TodoItem.objects.get(id=todo_id)
    item_to_edit.content= request.POST['content']
    item_to_edit.save()
    return HttpResponseRedirect('/todo/')

def updateTodo(request,todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    new_item = TodoItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')


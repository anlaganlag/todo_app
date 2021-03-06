"""editdojo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from  hello.views import myView
from todo.views import  (
    TodoList,
    TodoCreate,
    addTodo,
    deleteTodo,
    doneTodo,
    editTodo,
    updateTodo,
    mybinView,
    mydoneView,
    mybinclearView,
    mydoneclearView

)





urlpatterns = [
    path('admin/', admin.site.urls),
    path('say/',myView),
    path('bin/',mybinView,name='bin'),
    path('clearbin/',mybinclearView,name='clearbin'),
    path('cleardone/',mydoneclearView,name='cleardone'),
    path('done/',mydoneView,name='done'),
    path('todo/',TodoList.as_view(),name='todo'),
    path('create/',TodoCreate.as_view(),name='create'),
    path('addTodo/',addTodo),
    path('doneTodo/<int:todo_id>/',doneTodo),
    path('deleteTodo/<int:todo_id>/',deleteTodo),
    path('editTodo/<int:todo_id>/',editTodo),
    path('updateTodo/<int:todo_id>/',updateTodo),

]

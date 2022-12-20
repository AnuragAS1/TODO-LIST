from django.shortcuts import redirect, render
from .forms import TodoForm
from .models import TodoListItem 
from django.http import HttpResponse
from django.http import HttpResponseRedirect 
from django.views.generic import ListView,CreateView
from django.urls import reverse
from django.views import View
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
# from .models import GeeksModel

# def todoappView(request):
#     all_todo_items = TodoListItem.objects.all()
#     return render(request, 'j.html',
#     {'all_items':all_todo_items})


def todoappView(request):
    if request.method == 'GET':
        # <view logic>
        return HttpResponse('result')
    
class MyView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')
 
# def addTodoView(request):
#     # forms = request.POST['content']
#     # new_item = TodoListItem(content = forms)
#     # new_item.save()
#     # return HttpResponseRedirect('/todoapp/') 

#     forms = TodoForm(request.POST or None )
#     if forms.is_valid():
#         forms.save()
#         return redirect('/')
#     context = {
#         "forms": forms
#     }
#     return render(request,'add.html', context)

# def deleteTodoView(request, i):
#     note = TodoListItem.objects.get(id= i)
#     note.delete()
#     return HttpResponseRedirect('/todoapp/') 
class deleteTodoView(DeleteView):
    # specify the model you want to use
    model = TodoListItem
     
    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url ="/"
    template_name="classtodoapp/delete.html"

# def update(request, id):
#     todo = TodoListItem.objects.get(id=id)
#     form = TodoListItem(request.POST or None, instance=todo )
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     context = {
#         "form": form,
#     }
#     return HttpResponseRedirect('/todoapp/', context)

class TodolistView(ListView):
 
    # specify the model for list view
    model = TodoListItem 
    template_name="classtodoapp/list.html"
    # def get_success_url(self):
    #     return reverse('listr')
    



#     def get_success_url(self):
#         return reverse('test')

 
class TodoCreate(CreateView):
 
    # specify the model for create view
    model = TodoListItem
 
    # specify the fields to be displayed
 
    fields = ['title', 'description']
    template_name="classtodoapp/create.html"

class TodoDetails(DetailView):
    # specify the model to use
    model = TodoListItem
    template_name="classtodoapp/detail.html"

    
class TodoUpdate(UpdateView):
    # specify the model you want to use
    model = TodoListItem
    template_name="classtodoapp/update.html"
    # specify the fields
    fields = [
        "title",
        "description"
    ]
 
    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url ="/"
 
    
    # def get_success_url(self):
    #     return reverse('test')
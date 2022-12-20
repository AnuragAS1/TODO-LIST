from django.contrib import admin
from django.urls import path, include
from classtodoapp import views
from classtodoapp.views import todoappView,MyView,TodolistView,TodoCreate, TodoUpdate, TodoDetails, deleteTodoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todoapp/', todoappView,name="test"),
    path('', TodolistView.as_view(),name="listr"),
    # path('addTodoItem/', addTodoView), 
    path('about/', MyView.as_view()),
    # path('deleteTodoItem/<int:i>/', deleteTodoView), 
    # path('class/list',TodoCreate.as_view(),name="list_view"),
    path('create/', TodoCreate.as_view(),name="create-list" ),
    path('update/<int:pk>', TodoUpdate.as_view(), name="TodoUpdate"),
    path('details/<int:pk>', TodoDetails.as_view(),name="details" ),
    path('delete/<int:pk>', deleteTodoView.as_view(),name="test-delete"),
]
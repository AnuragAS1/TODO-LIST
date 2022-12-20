# from django import forms
# from.models import TodoListItem
# class TodoForm(forms.ModelForm):
#     class Meta:
#         model = TodoListItem
#         fields = ['id','content']


from django import forms
from .models import TodoListItem
 
 
# creating a form
class TodoForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = TodoListItem
 
        # specify fields to be used
        fields = [
            "title",
            "description",
        ]
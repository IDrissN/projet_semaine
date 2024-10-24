from .models import Todo
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

        labels = {
        "title" : "Titre",
        "todo" : "Description",
        }

        widgets ={
        "title" : forms.TextInput(attrs={"placeholder":"Entrez une tâche"}),
        "todo" : forms.TextInput(attrs={"placeholder":"Entrez une description de tâche"}), 
        }
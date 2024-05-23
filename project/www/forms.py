from django import forms

from .models import Project,Task,Comment

class ProjectForm(forms.ModelForm):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    description = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'Start Date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'End Date'}))
    photo = forms.ImageField(widget=forms.FileInput(attrs={'placeholder': 'Choose a photo'}))
    class Meta:
        model = Project
        fields = '__all__'


class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    description = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'Date'}))

    class Meta:
        model = Task
        fields = '__all__'        




class CommentForm(forms.ModelForm):
    author = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Author'}))
    content = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Content'}))

    class Meta:
        model = Comment
        fields = '__all__'
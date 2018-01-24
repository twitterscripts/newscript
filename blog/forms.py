from django import forms
from .models import Post
from django.forms import ModelForm, Textarea

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title', 'text',)
        widgets = {
            'text': Textarea(attrs={'cols': 18, 'rows': 2}),
        }





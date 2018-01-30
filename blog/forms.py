from django import forms
from .models import Post
from .models import BugReport
from django.forms import ModelForm, Textarea

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title', 'text',)
        labels = {
            'author': "Author :",
            'title': "Object / Title :",
            'text': "Message :",
        }

        widgets = {
            'text': Textarea(attrs={'cols': 18, 'rows': 2}),
        }


class ReportForm(forms.ModelForm):

    class Meta:
        model = BugReport
        fields = ('authorr', 'titler', 'textr',)
        labels = {
            'authorr': "Report Author :",
            'titler': "Report Object / Title :",
            'textr': "Report Problem :",
        }
        widgets = {
            'textr': Textarea(attrs={'cols': 18, 'rows': 2}),
        }





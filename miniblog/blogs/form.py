from django import forms

from .models import Article


class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter title',
                'class': 'form-control',
            }),
            'content': forms.TextInput(attrs={
                'placeholder': 'Enter content',
                'class': 'form-control',
            }),
        }

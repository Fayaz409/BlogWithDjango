from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model =Post
        fields=('title','title_tag','author','body')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control','placeholder':'Title tag'}),
            'body':forms.Textarea(attrs={'class':'form-control','placeholder':'Your Content Goes Here'}),
            'author':forms.Select(attrs={'class':'form-control','placeholder':'Author'}),
        }
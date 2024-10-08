from django import forms
from .models import Post,Category

choices=Category.objects.all().values_list('name','name')
choice_list=[]
for item in choices:
    choice_list.append(item)
class PostForm(forms.ModelForm):
    class Meta:
        model =Post
        fields=('title','title_tag','author','category','body')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control','placeholder':'Title tag'}),
            'body':forms.Textarea(attrs={'class':'form-control','placeholder':'Your Content Goes Here'}),
            # 'author':forms.Select(attrs={'class':'form-control','placeholder':'Author'}),
            'author':forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden','placeholder':'Your Name'}),
            'category':forms.Select(choices=choice_list, attrs={'class':'form-control','placeholder':'Category'}),
        }
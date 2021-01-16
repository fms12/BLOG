from django import forms
from django.forms import widgets
from .models import Post, Category
# choices=[('coding','coding'),('sports','sports'),('entainment','entainment')]
choices = Category.objects.all().values_list('name', 'name')
# it create dynamic category choices_list
choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body','snippet','header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control"}),
            'title_tag': forms.TextInput(attrs={'class': "form-control"}),
            'author': forms.TextInput(attrs={'class': "form-control",'value':'','id':'elder','type':'hidden'}),
            # 'author': forms.Select(attrs={'class': "form-control"}),
            # select is here to make dropdown
            'category': forms.Select( choices=choice_list, attrs={'class': "form-control"}),
            'body': forms.Textarea(attrs={'class': "form-control"}),
            'snippet':forms.Textarea(attrs={'class': "form-control"}),
            # give the snippet for your post
            
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body','snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Title'}),
            'title_tag': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Title_tag'}),
            # 'author':forms.Select(attrs={'class':"form-control",'placeholder':'Author' }),
            'body': forms.Textarea(attrs={'class': "form-control"}),
            'snippet': forms.Textarea(attrs={'class': "form-control"})
                    }

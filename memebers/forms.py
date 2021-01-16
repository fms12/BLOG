from blog.models import Profile
from django.contrib.auth.forms import UserChangeForm, UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms import fields, widgets


class ProfilePageForm(forms.ModelForm):


    class Meta:
        model = Profile
        fields =('BIO','profile_pic','website_url','facebook_url','twitter_url','instagram_url')
        widgets={
            # text area gives big area 
            #  text input gives  the  simple line box
            'BIO': forms.Textarea(attrs={'class': "form-control"}),
            # 'profile_pic': forms.TextInput(attrs={'class': "form-control"}),
            'website_url': forms.TextInput(attrs={'class': "form-control"}),
            'facebook_url': forms.TextInput( attrs={'class': "form-control"}),
            'twitter_url': forms.TextInput(attrs={'class': "form-control"}),
            'instagram_url':forms.TextInput(attrs={'class': "form-control"}),
            # give the snippet for your post
        }


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

########################################################################  this is classtype form creation #################################
# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(widget=forms.EmailInput(
#         attrs={'class': 'form-control'}))
#     first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
#     # last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))

#     class Meta:
#         model = User
#         fields = ('username', 'first_name',
#                   'email', 'password1', 'password2')

#     def __init__(self, *args, **kwargs):
#         super(SignUpForm, self).__init__(*args, **kwargs)

#         self.fields['username'].widget.attrs['class'] = 'form-control'
#         self.fields['email'].widget.attrs['class'] = 'form-control'
#         self.fields['password1'].widget.attrs['class'] = 'form-control'
#         self.fields['password2'].widget.attrs['class'] = 'form-control'



class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # is_superuser = forms.BooleanField( widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # is_staff = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # Old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email', 'is_active')


class PasswordchangingForm(PasswordChangeForm):
    old_password=forms.CharField( max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1=forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2=forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control'})) 


    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2')
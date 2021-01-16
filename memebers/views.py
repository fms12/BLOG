from django.views.generic.edit import CreateView
from blog.models import Profile
from memebers.forms import SignUpForm
from django.shortcuts import render,redirect
from django.contrib import messages

from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import EditProfileForm, PasswordchangingForm, ProfilePageForm, SignUpForm
#  for message 
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView



class CreateProfilePageView(CreateView):
    model= Profile
    form_class = ProfilePageForm
    template_name='registration/create_profile.html'
    
#  allow the  which user create profile than it pass the form to user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form) # save the form if the user fill it up
    

#  here you can edit and the  make profile of the user
class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    # feild for what we want in the feild
    fields =['BIO','profile_pic','website_url','facebook_url','twitter_url','instagram_url',]
    success_url = reverse_lazy('home')



class PasswordChangeView(PasswordChangeView):
    form_class = PasswordchangingForm
    # form_class = PasswordChangeForm
    # success_url= reverse_lazy('home') - #( redirect to the home page)
    success_url =reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html',{})





# def registerpage(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     else:
#         form = SignUpForm()
#         if request.method == 'post':
#             form  = SignUpForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 # thiss give the 
#                 user = form.cleaned_data.get('username')
#                 messages.success(request,'Account was created for ' + user)
#                 return redirect('login')
#         context ={'form': form}
#         return render(request,'registration/register.html',context)

class UserResgisterView(generic.CreateView,SuccessMessageMixin):
        form_class = SignUpForm
        template_name = 'registration/register.html'
        success_url = reverse_lazy('login')
        success_message = "%(username)s Account was created sucessfully"

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name='registration/edit_profile.html'
    success_url= reverse_lazy('home')


    def get_object(self):
        return self.request.user
        # send the current user to the web


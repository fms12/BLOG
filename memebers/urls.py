from .import views
from django.urls import path
from django.views.generic.base import TemplateView
from .views import CreateProfilePageView, EditProfilePageView,UserEditView,PasswordChangeView, UserResgisterView
# from django.contrib.auth import views as auth_views

urlpatterns = [
# this views.registerpage is here for def  in the url
# path('register/',view.registerpage, name='register'),

path('register/', UserResgisterView.as_view(), name='register'),
path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
# path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),

path('password/', PasswordChangeView.as_view(template_name='registration/change-password.html')),
path('password_success',views.password_success, name='password_success'),

path('<int:pk>/edit_profile_page/',EditProfilePageView.as_view(), name='edit_profile_page'),
path('create_profile/',CreateProfilePageView.as_view(), name='create_profile')

]


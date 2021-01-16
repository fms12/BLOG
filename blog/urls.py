from blog.models import Category
from django.urls import path
from django.views.generic.edit import DeleteView

from .views import AddPostView, CategoriesView, HomeView, ArticleView, UpdatePostView, DeletePostView, AddCategoryView,LikeView


urlpatterns = [
    # path('', views.index, name='index.html'),
    # instance of using the upperone import the views class home view and make the path
    # as_view is the function(class method) which will connect my MyView class with its url.
    path('', HomeView.as_view(), name='home'),
    # articel/<int:pk> give the http://127.0.0.1:8000/article/1 primary key like this as in last of the url
    path('article/<int:pk>', ArticleView.as_view(), name='article'),
    path("blog/", AddPostView.as_view(), name="blog"),
    path("category/", AddCategoryView.as_view(), name='category'),
    path("artice/update/<int:pk>", UpdatePostView.as_view(), name='update'),
    path("artice/<int:pk>/delete", DeletePostView.as_view(), name='delete'),
    path("categories/<str:cats>/", CategoriesView, name='categories'),
    path('like/<int:pk>', LikeView, name='like_post'),
]

from django.views.generic.edit import DeleteView
from blog.models import Post
from django.db import models
from .models import Category, Post
from django.shortcuts import render, get_object_or_404
# we can copy the database lsit of the post and the detail of the post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .form import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# def index(request):
#     return render(request, 'blog/index.html', {})

# we are using the  class instance of the def

################################################################


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        # if post like than filter the user with id an check does it if it exits 
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article', args=[str(pk)]))


class HomeView(ListView):
    model = Post  # here create model val for the post
    template_name = "blog/home.html"  # here the html content
    # ordering = ['-id']  # it make the post in the descending order so the we can easly see the latest blog at first
    ordering = ['-post_date']  # here order the post according the date.

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(**kwargs)
        context['cat_menu'] = cat_menu
        return context


class ArticleView(DetailView):
    model = Post
    template_name = "blog/article.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleView, self).get_context_data(**kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['cat_menu'] = cat_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        #  context access on the web page
        return context


def CategoriesView(request, cats):
    category_post = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'blog/categories.html', {'cats': cats.title().replace('-', ' '), 'category_post': category_post})


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/blog.html"
    # in __all__ we get all models
    # fields= '__all__'
#fields=('title', 'body',)
    # here we get only title and body

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddPostView, self).get_context_data(**kwargs)
        context['cat_menu'] = cat_menu
        return context


class AddCategoryView(CreateView):
    model = Category
    template_name = 'blog/category.html'
    fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategoryView, self).get_context_data(**kwargs)
        context['cat_menu'] = cat_menu
        return context


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "blog/update.html"
    # fields = ['title','title_tag','body']


class DeletePostView(DeleteView):
    model = Post
    template_name = "blog/delete.html"
    #  it back the url to the home after delete the  post
    success_url = reverse_lazy('home')

from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
from django.views.generic import ListView,DeleteView,UpdateView,CreateView,DetailView
# Create your views here.
# def index(request):
#     return render(request,'blogapp/index.html')

class PostView(ListView):
    model = Post
    template_name='blogapp/index.html'
    ordering=['-post_date']

class DetailPost(DetailView):
    model=Post
    template_name='blogapp/detail_post.html'

class UpdatePost(UpdateView):
    model= Post
    form_class=PostForm
    template_name='blogapp/update_post.html'
    # fields=['title','title_tag','body']

class CreatePost(CreateView):
    model= Post
    form_class=PostForm
    template_name='blogapp/create_post.html'
    # fields='__all__'

class DeletePost(DeleteView):
    model=Post
    template_name='blogapp/delete_post.html'
    success_url=reverse_lazy('home')



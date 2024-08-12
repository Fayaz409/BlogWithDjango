from django.shortcuts import render,get_object_or_404
from .models import Post,Category
from .forms import PostForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView,DeleteView,UpdateView,CreateView,DetailView
# Create your views here.
# def index(request):
#     return render(request,'blogapp/index.html')

def LikeView(request, pk):
    post = get_object_or_404(Post, id=pk)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('detail_post', args=[str(pk)]))


class PostView(ListView):
    model = Post
    template_name = 'blogapp/index.html'
    ordering = ['-post_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Category.objects.all()
        # Add a flag to each post to indicate whether the user has liked it
        if self.request.user.is_authenticated:
            for post in context['object_list']:
                post.is_liked = post.likes.filter(id=self.request.user.id).exists()
        return context


class DetailPost(DetailView):
    model = Post
    template_name = 'blogapp/detail_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context['total_likes'] = total_likes
        if self.request.user.is_authenticated:
            context['is_liked'] = stuff.likes.filter(id=self.request.user.id).exists()
        return context


class UpdatePost(UpdateView):
    model= Post
    form_class=PostForm

    template_name='blogapp/update_post.html'
    # fields=['title','title_tag','body']
    
    

class AddCategory(CreateView):
    model=Category
    template_name='blogapp/add_category.html'
    fields='__all__'
class CreatePost(CreateView):
    model= Post
    form_class=PostForm
    template_name='blogapp/create_post.html'
    # fields='__all__'

def CategoryView(request, cats):
    category_posts=Post.objects.filter(category=cats)
    return render(request,'blogapp/category_detail.html',{'cats':cats,'category_posts':category_posts}) 

class DeletePost(DeleteView):
    model=Post
    template_name='blogapp/delete_post.html'
    success_url=reverse_lazy('home')



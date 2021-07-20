
from django.shortcuts import render, redirect
#from django.contrib.auth.decorators import login_required
#from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
#utilities
from posts.forms import PostForm
from posts.models import Post
# Create your views here.

class PostsFeedView(LoginRequiredMixin, ListView):
    template_name='posts/feed.html'
    model=Post
    ordering=('-created',)
    paginate_by=30
    context_object_name='posts'

class PostDetailView(LoginRequiredMixin,DetailView):
    template_name='posts/detail.html'
    queryset=Post.objects.all()
    context_object_name='post'

class CreatePostView(LoginRequiredMixin,CreateView):
    template_name='posts/new.html'
    form_class=PostForm
    success_url=reverse_lazy('posts:feed')

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['user']=self.request.user
        context['profile']=self.request.user.profileuser
        return context

"""@login_required
def list_posts(req):
    posts = Post.objects.all().order_by('-created')
    return render(req,'posts/feed.html', {'posts':posts})
"""





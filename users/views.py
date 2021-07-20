from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.utils import IntegrityError

from django.views.generic import DetailView
from django.views.generic import FormView
from django.views.generic import UpdateView

from users.models import ProfileUser

from users.forms import SignupForm

from django.contrib.auth.models import User
from posts.models import Post
# Create your views here.
#req == request

class UserDetailView(LoginRequiredMixin,DetailView):
    template_name='users/detail.html'
    slug_field='username'
    slug_url_kwarg='username'
    queryset= User.objects.all()
    context_object_name='user'

    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        user= self.get_object()
        context['posts']= Post.objects.filter(user=user).order_by('-created')
        return context


class UpdateProfileView(LoginRequiredMixin,UpdateView):
    template_name='users/update_profile.html'
    model=ProfileUser
    fields=['website','biography','phone','picture']

    def get_object(self):
        return self.request.user.profileuser

    def get_success_url(self):
        username=self.object.user.username
        return reverse('users:detail',kwargs={'username':username})



class SignupView(FormView):
    template_name='users/signup.html'
    form_class=SignupForm
    success_url=reverse_lazy('users:login')

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)

class LoginView(auth_views.LoginView):
    template_name='users/login.html'

class LogoutView(LoginRequiredMixin,auth_views.LogoutView):
    template_name='users/logout.html'




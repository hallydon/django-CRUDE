from pdb import post_mortem
from pyexpat import model
from django.views.generic.list import ListView
from django.views.generic.edit import CreatView
from django.views.generic.Detail import DetailView
from django.views.generic.PostUpdateView import PostUpdateView
from django.views.generic.PostDeleteView import PostDeleteView
from .models import BlogApp

class BlogAppListView(ListView):
    model = Post

class BlogAppCreatView(CreatView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

class BlogAppDetailView(DetailView):
    model = Post

class BlogAppPostUpdateView(PostUpdateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")


class BlogAppPostDeleteView(PostDeleteView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")







# Create your views here.

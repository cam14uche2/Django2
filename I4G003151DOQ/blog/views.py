from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

class blogListView(ListView):
    model = Post
    template_name = 'post_list.html'


class blogCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")



class blogDetailView(DetailView):
    model =Post
    template_name = 'post_Detail.html'

class blogUpdateView(UpdateView):
    model: Post
    fields: "__all__"
    success_url = reverse_lazy("blog:all")


class blogDeleteView(DeleteView):
    model: Post
    template_name = 'post_confirm_delete.html'
    fields = "__all__"
    success_urls = reverse_lazy("blog:all")        




from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from apps.api.models import Post, Comment
from apps.api.forms import CommentForm


class PostView(ListView):
    model = Post
    template_name = "post/post_list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "post/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_id = self.kwargs['pk']
        context["comments"] = Comment.objects.filter(post=post_id).order_by("-created_at")
        context["form"] = CommentForm()

        return context


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment/comment_form.html'

    def form_valid(self, form):
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['post'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('api:post_detail', kwargs={'pk': self.kwargs['post']})
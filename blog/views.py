from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Comment, Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import PostCreateForm, CommentCreateForm


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-is_pinned','-date_posted']
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detailed.html'
    context_object_name = 'post'

    # TODO: to be fixed
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = CommentCreateForm

    #     return context

    # def get(self, request, *args, **kwargs):
    #     form = CommentCreateForm()
    #     self.object = self.get_object()
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = CommentCreateForm

    #     return self.render_to_response(context=context)

    # def post(self, request, *args, **kwargs):
    #     form = CommentCreateForm(request.POST)

    #     if form.is_valid():
    #         comment = form.save(commit=False)
    #         comment.owner = request.user
    #         comment.post = self.get_object()
    #         comment.save()
    #         self.object = self.get_object()
    #         context = super().get_context_data(**kwargs)
    #         context['form'] = CommentCreateForm

    #     else:
    #         self.object = self.get_object()
    #         context = super().get_context_data(**kwargs)
    #         context['form'] = form


    #     return self.render_to_response(context=context)


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    template_name = 'blog/create.html'
    context_object_name = 'post'
    form_class = PostCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_editor

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        return (self.request.user.is_editor and self.request.user == post.author)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'is_pinned', 'image']
    template_name = 'blog/update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return (self.request.user.is_editor and self.request.user == post.author)
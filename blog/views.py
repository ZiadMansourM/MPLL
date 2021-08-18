from django.shortcuts import render, redirect
from django.views.generic import (
    ListView, DetailView, CreateView, 
    UpdateView, DeleteView, FormView
    )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Comment, Post
from .forms import PostCreateForm, CommentCreateForm, ReplyCreateForm, ContactUsForm


def contact_us(request):
    if request.POST:
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'your message has been sent successfully')
            return redirect('blog-home')
    form = ContactUsForm()
    context = {
        'form': form
    }
    return render(request, 'blog/contact_us.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-is_pinned','-date_posted']
    paginate_by = 5


class CommentCreateView(LoginRequiredMixin, FormView):
    form_class = CommentCreateForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.post = Post.objects.get(id=self.kwargs['pk'])
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('blog-detail', kwargs={'pk': self.kwargs['pk']})
    
    def get_template_names(self):
        return ['blog/empty_form.html']


class ReplyCreateView(LoginRequiredMixin, FormView):
    form_class = ReplyCreateForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.comment = Comment.objects.get(id=self.kwargs['id'])
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('blog-detail', kwargs={'pk': self.kwargs['pk']})
    
    def get_template_names(self):
        return ['blog/empty_form.html']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detailed.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentCreateForm
        return context


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
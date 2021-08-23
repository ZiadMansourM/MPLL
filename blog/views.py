from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.views.generic import (
    ListView, DetailView, CreateView, 
    UpdateView, DeleteView, FormView
    )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse_lazy, reverse
from .models import Comment, Post, Reply, Report
from .forms import PostCreateForm, CommentCreateForm, ReplyCreateForm, ContactUsForm
from django.http import HttpResponseRedirect


@require_http_methods(["POST"])
def report(request):
    uuid = request.POST['id']
    message = request.POST['message']
    domain = get_current_site(request).domain
    url = "http://" + domain + "/"
    try:
        post = Post.objects.get(id=uuid)
        url += f"blog/{post.id}"
        entity = "Post"
    except ObjectDoesNotExist:
        try:
            comment = Comment.objects.get(id=uuid)
            post_id = request.POST['post_id']
            url += f"blog/{post_id}/comment/{comment.id}"
            entity = "Comment"
        except ObjectDoesNotExist:
            try:
                reply = Reply.objects.get(id=uuid)
                comment_id = request.POST['comment_id']
                post_id = request.POST['post_id']
                url += f"blog/{post_id}/comment/{comment_id}/reply/{reply.id}"
                entity = "Reply"
            except:
                raise Exception("Invalid Please try again")
    
    Report.objects.create(entity=entity, url=url, message=message)
    
    messages.success(request, 'Thanks, we have received your Report and will be reviewed ASAP')
    return redirect('blog-home')

def contact_us(request):
    if request.POST:
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'your message has been sent successfully')
            return redirect('blog-home')
    else:
        form = ContactUsForm()
    context = {
        'form': form
    }
    return render(request, 'blog/contact_us.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 7

    def get_queryset(self):
        query = self.request.GET.get('searchkey')
        if query:
            return self.model.objects.filter(title__icontains=query)
        else:
            return self.model.objects.all()


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
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context['form'] = CommentCreateForm
        context['total_likes'] = total_likes
        return context

class CommentDetailView(DetailView):
    model = Comment
    template_name = 'blog/comment-detailed.html'
    context_object_name = 'comment'

    def get_object(self, queryset=None):
        return get_object_or_404(Comment, pk=self.kwargs['id'])


class ReplyDetailView(DetailView):
    model = Post
    template_name = 'blog/reply-detailed.html'
    context_object_name = 'reply'

    def get_object(self, queryset=None):
        return get_object_or_404(Reply, pk=self.kwargs['num'])


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


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('blog-detail', args=[str(pk)]))
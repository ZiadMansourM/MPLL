from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth import get_user_model

from .models import Post, Comment

User = get_user_model()

class CommmentJsonCreateView(LoginRequiredMixin, UserPassesTestMixin, View):
    def post(self, *args, **kwargs):
        comment_message = self.request.POST['comment']
        print(comment_message)
        comment = Comment(comment=comment_message)
        comment.owner = self.request.user
        comment.post = Post.objects.get(id=self.kwargs['pk'])
        comment.save()
        # image.url
        # owner.username
        # comment.id
        response_dict = {
            'image_url': comment.owner.image.url,
            'owner_username': comment.owner.username,
            'comment_id': comment.id,
            'comment': comment.comment
        }
        return JsonResponse(response_dict, safe=False)

    def test_func(self):
        return (self.request.user.is_editor)


class CommmentJsonListView(View):
    def get(self, *args, **kwargs):
        comments = list(Comment.objects.filter(post=self.kwargs['pk']).values())
        return JsonResponse(comments, safe=False)
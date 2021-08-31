from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth import get_user_model

from .models import Post, Comment, Reply

User = get_user_model()

class CommmentJsonCreateView(LoginRequiredMixin, View):
    def post(self, *args, **kwargs):
        comment_message = self.request.POST['comment']
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


class CommmentJsonListView(View):
    def get(self, *args, **kwargs):
        comments = list(Comment.objects.filter(post=self.kwargs['pk']).values())
        return JsonResponse(comments, safe=False)


class ReplyJsonCreateView(LoginRequiredMixin, View):
    def post(self, *args, **kwargs):
        reply_message = self.request.POST['reply']
        reply = Reply(reply=reply_message)
        reply.owner = self.request.user
        reply.comment = Comment.objects.get(id=self.request.POST['comment_id'])
        reply.save()
        # image.url
        # owner.username
        # comment.id
        response_dict = {
            'image_url': reply.owner.image.url,
            'owner_username': reply.owner.username,
            'reply_id': reply.id,
            'reply': reply.reply,
            'post_id':reply.comment.post.id,
            'comment_id':reply.comment.id,
            # 'reply_owner':reply.owner,
            # 'current_user':User,
        }
        return JsonResponse(response_dict, safe=False)
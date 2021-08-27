from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from blog.views import CommentCreateView, DeleteComment, PostDeleteView, PostListView, PostUpdateView, ReplyDetailView, contact_us, report
# Create your tests here.


class TestUrls(SimpleTestCase):

    # path('', PostListView.as_view(), name='blog-home'),
    def test_bloghome_url_is_resolved(self):
        url = reverse('blog-home')
        self.assertEquals(resolve(url).func.view_class, PostListView)

    # path('contactus/', contact_us, name="contact-us"),
    def test_contactus_url_is_resolved(self):
        url = reverse('contact-us')
        self.assertEquals(resolve(url).func, contact_us)

    # path('report/', report, name="report"),
    def test_report_url_is_resolved(self):
        url = reverse('report')
        self.assertEquals(resolve(url).func, report)

    # # path('<uuid:pk>/update', PostUpdateView.as_view(), name='blog-update'),
    # def test_blogupdate_url_is_resolved(self):
    #     url = reverse('blog-update',args=['some-post'])
    #     self.assertEquals(resolve(url).func.view_class, PostUpdateView)

    # # path('<uuid:pk>/delete', PostDeleteView.as_view(), name='blog-delete'),
    # def test_blogdelete_url_is_resolved(self):
    #     url = reverse('blog-delete',args=['some-post'])
    #     self.assertEquals(resolve(url).func.view_class, PostDeleteView)

    # # path('<uuid:pk>/comment/', CommentCreateView.as_view(), name='comment-create'),
    # def test_commentcreate_url_is_resolved(self):
    #     url = reverse('comment-create',args=['some-comment'])
    #     self.assertEquals(resolve(url).func.view_class, CommentCreateView)
        
    # # path('<uuid:pk>/comment/<uuid:id>/delete', DeleteComment, name='comment-delete'),
    # def test_commentdelete_url_is_resolved(self):
    #     url = reverse('comment-delete',args=['some-comment'])
    #     self.assertEquals(resolve(url).func, DeleteComment)

    # # path('<uuid:pk>/comment/<uuid:id>/reply/<uuid:num>', ReplyDetailView.as_view(), name='Comment-detail'),
    # def test_Commentdetail_is_resolved(self):
    #     url = reverse('Comment-detail')
    #     self.assertEquals(resolve(url).func.view_class, ReplyDetailView)

    # # path('<uuid:pID>/comment/<uuid:cID>/reply/<uuid:rID>/delete', DeleteReply, name='reply-delete'),
    #  def test_report_url_is_resolved(self):
    #     url = reverse('report')
    #     self.assertEquals(resolve(url).func, report)
    # # path('<uuid:pk>/comment/<uuid:id>', CommentDetailView.as_view(), name='Comment-detail'),
    #  def test_report_url_is_resolved(self):
    #     url = reverse('report')
    #     self.assertEquals(resolve(url).func, report)
    # # path('<uuid:pk>/', PostDetailView.as_view(), name='blog-detail'),
    #  def test_report_url_is_resolved(self):
    #     url = reverse('report')
    #     self.assertEquals(resolve(url).func, report)
    # # path('new/', PostCreateView.as_view(), name='blog-create'),
    #  def test_report_url_is_resolved(self):
    #     url = reverse('report')
    #     self.assertEquals(resolve(url).func, report)
    # # path('reports/',ReportListView.as_view(),name='report-list'),
    #  def test_report_url_is_resolved(self):
    #     url = reverse('report')
    #     self.assertEquals(resolve(url).func, report)
    # # path('like/<uuid:pk>/', LikeView, name='like-post'),
    #  def test_report_url_is_resolved(self):
    #     url = reverse('report')
    #     self.assertEquals(resolve(url).func, report)
    # # path('<uuid:pk>/comment/<uuid:id>/like', CommentLikeView, name='like-comment'),
    #  def test_report_url_is_resolved(self):
    #     url = reverse('report')
    #     self.assertEquals(resolve(url).func, report)
    # # path('<uuid:pk>/comment/<uuid:id>/reply/<uuid:num>/like', ReplyLikeView, name='like-reply'),
    #  def test_report_url_is_resolved(self):
    #     url = reverse('report')
    #     self.assertEquals(resolve(url).func, report)

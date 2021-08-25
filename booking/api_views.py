from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import View
from django.http import HttpResponse, JsonResponse

from .models import Author, Publisher,City
from .forms import AuthorCreateForm, PublisherCreateForm


class AuthorListJsonView(View):
    def get(self, *args, **kwargs):
        authors = list(Author.objects.values())
        return JsonResponse(authors, safe=False)


class AuthorCreateJsonView(LoginRequiredMixin, UserPassesTestMixin, View):
    def post(self, *args, **kwargs):
        name = self.request.POST['name']
        author = Author.objects.create(name=name)
        author = list(Author.objects.filter(name=name).values())
        return JsonResponse(author, safe=False)

    def test_func(self):
        return (self.request.user.is_editor)


class PublisherCreateJsonView(LoginRequiredMixin, UserPassesTestMixin, View):
    def post(self, *args, **kwargs):
        name = self.request.POST['name']
        publisher = Publisher.objects.create(name=name)
        publisher = list(Publisher.objects.filter(name=name).values())
        return JsonResponse(publisher, safe=False)

    def test_func(self):
        return (self.request.user.is_editor)


class CityCreateJsonView(LoginRequiredMixin, UserPassesTestMixin, View):

    def post(self, *args, **kwargs):
        name = self.request.POST['name']
        city = City.objects.create(name=name)
        city = list(City.objects.filter(name=name).values())
        return JsonResponse(city, safe=False)

    def test_func(self):
        return (self.request.user.is_editor)

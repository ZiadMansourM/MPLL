from django.shortcuts import render
from booking.models import City, DeweyDecimalClassification, Book, Author, Publisher
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import AuthorCreateForm, AuthorUpdateForm, BookCreateForm, CityCreateForm, PublisherCreateForm, PublisherUpdateForm
from django.db.models import Q

# Create your views here.


class BookListView(ListView):
    model = Book
    template_name = 'booking/home.html'
    context_object_name = 'books'
    paginate_by = 6   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['codes'] = DeweyDecimalClassification.objects.all()
        context['title'] = 'Booking'
        return context

    def get_queryset(self):
        query = self.request.GET.get('searchkey')
        category = self.request.GET.get("category")
        filters = Q()
        if category:
            filters &= Q(classification__family_num=category)
        if query:
            filters &= Q(name__icontains=query)
        return self.model.objects.filter(filters).distinct().order_by('-id')


class BookDetailView(DetailView):
    model = Book
    template_name = 'booking/detailed.html'
    context_object_name = 'book'


class BookCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Book
    template_name = 'booking/create.html'
    context_object_name = 'book'
    form_class = BookCreateForm

    def get_context_data(self, **kwargs):
        context = super(BookCreateView, self).get_context_data(**kwargs)
        context['author_form'] = AuthorCreateForm
        context['publisher_form'] = PublisherCreateForm
        return context

    def test_func(self):
        return self.request.user.is_librarian


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    success_url = '/booking'
    template_name = 'booking/book_confirm_delete.html'

    def test_func(self):
        return (self.request.user.is_librarian)


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['name', 'author', 'classification', 'code',
              'pages_num', 'date_published', 'date_added', 'publisher',
              'available_copies', 'available_borrowing', 'available',
              'image', 'brief']
    template_name = 'booking/update.html'

    def test_func(self):
        return (self.request.user.is_librarian)

# Author related views


class AuthorListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Author
    template_name = 'booking/author-list.html'
    context_object_name = 'authors'
    ordering = ('name',)
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'authors'
        return context

    def test_func(self):
        return self.request.user.is_librarian
# class AuthorDetailView(DetailView):
#     model = Author
#     template_name = 'booking/author-detailed.html'
#     context_object_name = 'author'


class AuthorCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Author
    template_name = 'booking/author-create.html'
    context_object_name = 'author'
    form_class = AuthorCreateForm

    def get_context_data(self, **kwargs):
        context = super(AuthorCreateView, self).get_context_data(**kwargs)
        context['city_form'] = CityCreateForm
        return context

    def test_func(self):
        return self.request.user.is_librarian


class AuthorDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Author
    # TODO:changing success url
    success_url = '/booking/authors'
    template_name = 'booking/author_confirm_delete.html'

    def test_func(self):
        return (self.request.user.is_librarian)


class AuthorUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Author
    # removed because Specifying both 'fields' and 'form_class' is not permitted.
    # fields = ['name', 'image', 'bio', 'birth_place', ]
    template_name = 'booking/author-update.html'
    form_class = AuthorUpdateForm

    def get_context_data(self, **kwargs):
        context = super(AuthorUpdateView, self).get_context_data(**kwargs)
        context['city_form'] = CityCreateForm
        return context

    def test_func(self):
        return (self.request.user.is_librarian)

# Publisher related views


class PublisherListView(ListView):
    model = Publisher
    template_name = 'booking/Publisher-list.html'
    context_object_name = 'Publishers'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Publishers'
        return context


# class AuthorDetailView(DetailView):
#     model = Author
#     template_name = 'booking/author-detailed.html'
#     context_object_name = 'author'


class PublisherCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Publisher
    template_name = 'booking/publisher-create.html'
    context_object_name = 'author'
    form_class = PublisherCreateForm

    def test_func(self):
        return self.request.user.is_librarian


class PublisherDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Publisher
    # TODO:changing success url
    success_url = '/booking/publishers'
    template_name = 'booking/publisher_confirm_delete.html'

    def test_func(self):
        return (self.request.user.is_librarian)


class PublisherUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Publisher
    template_name = 'booking/publisher-update.html'
    form_class = PublisherUpdateForm

    # def get_context_data(self, **kwargs):
    #     context = super(PublisherUpdateView, self).get_context_data(**kwargs)
    #     context['city_form'] = CityCreateForm
    #     return context

    def test_func(self):
        return (self.request.user.is_librarian)

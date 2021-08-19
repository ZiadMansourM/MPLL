from django.shortcuts import render
from booking.models import DeweyDecimalClassification, Book
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import BookCreateForm

# Create your views here.



class BookListView(ListView):
    model = Book
    template_name = 'booking/home.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['codes'] = DeweyDecimalClassification.objects.all()
        context['title'] = 'Booking'
        return context

class BookDetailView(DetailView):
    model=Book
    template_name = 'booking/detailed.html'
    context_object_name = 'book'

class BookCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Book
    template_name = 'booking/create.html'
    context_object_name = 'book'
    form_class = BookCreateForm

    def test_func(self):
        return self.request.user.is_editor

class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    success_url = '/booking'
    template_name = 'booking/book_confirm_delete.html'

    def test_func(self):
        return (self.request.user.is_editor)


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields =  ['name', 'author', 'classification', 'code',
                  'pages_num', 'date_published', 'date_added', 'publisher',
                  'available_copies', 'available_borrowing', 'available',
                  'image', 'brief']
    template_name = 'booking/update.html'

    def test_func(self):
        return (self.request.user.is_editor)

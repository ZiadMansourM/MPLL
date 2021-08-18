from django.shortcuts import render
from booking.models import Code, Book
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.


# def home(request):
#     codes=Code.objects.all()
#     return render(request, 'booking/home.html', {
#         'title': 'booking',
#         'codes': codes
#     })


class BookListView(ListView):
    model = Book
    template_name = 'booking/home.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['codes'] = Code.objects.all()
        context['title'] = 'Booking'
        return context

class BookDetailView(DetailView):
    model=Book
    template_name = 'booking/detailed.html'
    context_object_name = 'book'


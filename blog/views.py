from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from blog.models import Page
from pytils.translit import slugify


class PageCreateView(CreateView):
    model = Page
    fields = ('title', 'body', 'is_published',)
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_pag = form.save()
            new_pag.slug = slugify(new_pag.title)
            new_pag.save()
        return super().form_valid(form)


class PageUpdateView(UpdateView):
    model = Page
    fields = ('title', 'body', 'is_published',)
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_pag = form.save()
            new_pag.slug = slugify(new_pag.title)
            new_pag.save()
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse('blog:view', args=[self.kwargs.get('pk')])
    

class PageListView(ListView):
    model = Page

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)  
        queryset = queryset.filter(is_published=True)
        return queryset


class PageDetailView(DetailView):
    model = Page

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class PageDeleteView(DeleteView):
    model = Page    
    success_url = reverse_lazy('blog:list')

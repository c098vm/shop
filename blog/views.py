from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from blog.models import Post


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'content', 'preview', 'publication_attribute',)
    success_url = reverse_lazy('blog:posts')

    def form_valid(self, form):
        if form.is_valid():
            new_form = form.save()
            new_form.slug = slugify(new_form.title)
            new_form.save()
            return super().form_valid(form)


class PostListView(ListView):
    model = Post
    extra_context = {'title': 'Посты'}

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(publication_attribute=True)
        return queryset


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object

class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'content', 'preview', 'publication_attribute',)

    # success_url = reverse_lazy('blog:posts')

    def get_success_url(self):
        return reverse('blog:post', args=[self.object.pk])


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:posts')

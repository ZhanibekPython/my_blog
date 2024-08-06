from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.base import View, TemplateView

from .forms import NewEventForm, NewAuthorForm
from .models import Article, Author


class Index(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Article.objects.all()
        return context


# class GetPostBySlug(View):
#     def get(self, request, slug: str):
#         the_post = get_object_or_404(Article, slug=slug)
#         other_posts = the_post.author.article_set.exclude(slug=slug)
#         return render(request, 'blog/post_by_slug.html', {'post': the_post, 'other_posts': other_posts})

class GetPostBySlug(DetailView):
    template_name = 'blog/post_by_slug.html'
    model = Article
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()
        author = article.author
        other_posts = Article.objects.filter(author=author).exclude(slug=article.slug)
        context['other_posts'] = other_posts
        return context


def upload_files(file):
    with open(f"uploads/{file.name}", "wb+") as destination:
        for part in file.chunks():
            destination.write(part)


def file_upload(request):
    if request.method == 'POST':
        upload_files(request.FILES['file'])
        redirect('main')
    return render(request, 'blog/image_uploader.html', {'title': 'Download file'})


class NewEvent(View):
    def get(self, request):
        form = NewEventForm()
        return render(request, 'blog/new_event.html', {'title': 'Новое событие', 'form': form})

    def post(self, request):
        form = NewEventForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            date_publ = form.cleaned_data['date_publ']
            content = form.cleaned_data['content']
            author = form.cleaned_data['author']
            try:
                Article.objects.create(name=name, date_publ=date_publ, content=content, author=author,
                                       description=description)
            except:
                form.add_error(None, "Error occured dirung uploading or saving data from the form")
            return redirect(reverse('home'))

        return render(request, 'blog/new_event.html', {'title': 'Новое событие', 'form': form})


class NewAuthor(View):
    def get(self, request):
        form = NewAuthorForm()
        return render(request, 'blog/new_author.html', {'title': 'Новый автор', 'form': form})

    def post(self, request):
        form = NewAuthorForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            birth_date = form.cleaned_data['birth_date']
            birth_place = form.cleaned_data['birth_place']

            Author.objects.create(full_name=full_name, birth_date=birth_date, birth_place=birth_place)

        return render(request, 'blog/new_author.html', {'title': 'Новый автор', 'form': form})


class AllPosts(ListView):
    template_name = 'blog/all_posts.html'
    model = Article
    ordering = ['date_publ']


def page_not_found(request, exception):
    return render(request, 'page_not_found.html')


def server_error(request):
    return render(request, 'server_error.html')

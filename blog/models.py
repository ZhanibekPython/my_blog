from django.db import models
from django.utils.text import slugify


class Author(models.Model):
    full_name = models.CharField('ФИО автора', max_length=40)
    birth_date = models.DateField(verbose_name='Дата рождения', null=False, blank=False)
    birth_place = models.CharField(max_length=30)

    def __str__(self):
        return self.full_name


class Article(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название')
    description = models.CharField(max_length=100, verbose_name='Описание', default='')
    date_publ = models.DateField(auto_now=True, verbose_name='Дата публикации')
    content = models.TextField(default='This is a fake text for this article', verbose_name='Текст статьи')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    slug = models.SlugField(default='')
    image = models.ImageField(upload_to='blog/img/', null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}, {self.author}, {self.date_publ}'

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('post_by_slug', kwargs={'slug': self.slug})
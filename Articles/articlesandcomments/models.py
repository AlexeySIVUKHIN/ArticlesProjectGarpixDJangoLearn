from django.db import models
from django.urls import reverse


class Articles(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(blank=True, verbose_name='Текст')
    slug = models.SlugField(verbose_name='ЧПУ', blank = True, null = True, unique=True)
    def __str__(self):
        return self.title
    def get_comments(self):
        return self.comment_art.all()
    def get_absolute_url(self):
        return reverse('article', kwargs={'art_slug': self.slug})

class Comment(models.Model):
    name = models.CharField(max_length=255, verbose_name='Автор комментария')
    text = models.TextField(blank=True, verbose_name='Текст комментария')
    art = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='comment_art', verbose_name="Исходная статья", blank=True, null=True)
    def __str__(self):
        return f'{self.name} : {self.text}'
    # def is_valid_comment(self):
    #     return (self.text != self.name)
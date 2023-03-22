from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(blank=True, verbose_name='Текст')

    def __str__(self):
        return self.title

    def GetComments(self):
        return self.comment_art.all()

class Comment(models.Model):
    name = models.CharField(max_length=255, verbose_name='Автор комментария')
    text = models.TextField(blank=True, verbose_name='Текст комментария')
    art = models.ForeignKey('Articles', on_delete=models.CASCADE, related_name='comment_art', verbose_name='Статья')

    def __str__(self):
        return self.name, self.text
# Generated by Django 4.1.7 on 2023-03-26 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articlesandcomments', '0005_comment_art_alter_comment_name_alter_comment_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='ЧПУ'),
        ),
    ]

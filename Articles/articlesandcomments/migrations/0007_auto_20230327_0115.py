# Generated by Django 2.2 on 2023-03-26 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articlesandcomments', '0006_articles_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
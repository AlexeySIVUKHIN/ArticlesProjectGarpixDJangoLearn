# Generated by Django 4.1.7 on 2023-03-27 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articlesandcomments', '0007_auto_20230327_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
# Generated by Django 3.1.3 on 2020-12-12 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0002_article_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='likes',
        ),
    ]

# Generated by Django 3.1 on 2020-10-12 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='blog_content',
            field=models.TextField(),
        ),
    ]

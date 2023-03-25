# Generated by Django 3.2.8 on 2022-04-13 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_singer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.AddField(
            model_name='article',
            name='signer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.singer'),
        ),
    ]

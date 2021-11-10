# Generated by Django 3.2.8 on 2021-11-10 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20211109_1110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reader',
            name='book_title',
        ),
        migrations.RemoveField(
            model_name='reader',
            name='user_id',
        ),
        migrations.AddField(
            model_name='reader',
            name='book',
            field=models.ForeignKey(db_column='book_title', default=1, on_delete=django.db.models.deletion.CASCADE, related_name='read_rows', to='blog.book', verbose_name='link to book'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reader',
            name='user',
            field=models.ForeignKey(db_column='user_id', default=2, on_delete=django.db.models.deletion.CASCADE, related_name='read_rows', to='auth.user', verbose_name='link to user'),
            preserve_default=False,
        ),
    ]
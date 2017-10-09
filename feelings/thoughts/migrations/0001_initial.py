# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Thought',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('recorded_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('condition', models.IntegerField(choices=[(0, 'Ecstatic'), (5, 'Passionate'), (10, 'Happy'), (15, 'Optimistic'), (20, 'Content'), (25, 'Bored'), (26, 'Tired'), (27, 'Hungry'), (30, 'Pessimistic'), (35, 'Frustrated'), (40, 'Overwhelmed'), (45, 'Disappointed'), (50, 'Worried'), (55, 'Angry'), (60, 'Jealous'), (65, 'Insecure'), (70, 'Guilty'), (75, 'Fear'), (80, 'Grief'), (85, 'Despair')])),
                ('notes', models.TextField(blank=True, default='')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='thoughts')),
            ],
        ),
    ]

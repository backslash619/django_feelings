# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thoughts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thought',
            name='condition',
            field=models.IntegerField(choices=[(0, 'Ecstatic'), (5, 'Passionate'), (10, 'Happy'), (15, 'Optimistic'), (20, 'Content'), (25, 'Bored'), (26, 'Tired'), (27, 'Hungry'), (30, 'Pessimistic'), (35, 'Frustrated'), (40, 'Overwhelmed'), (45, 'Disappointed'), (50, 'Worried'), (55, 'Angry'), (60, 'Jealous'), (65, 'Insecure'), (70, 'Guilty'), (75, 'Fear'), (80, 'Grief'), (85, 'Despair'), (90, 'Paranoid')]),
        ),
    ]

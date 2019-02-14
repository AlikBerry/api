# Generated by Django 2.1.5 on 2019-02-14 07:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190211_0750'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myuser',
            options={'verbose_name': 'Profile', 'verbose_name_plural': 'Profiles'},
        ),
        migrations.RemoveField(
            model_name='wishes',
            name='title',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(help_text='Tələb olunur. 100 simvol və ya az. Hərflər, Rəqəmlər və @/./+/-/_ simvollar.', max_length=100, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Düzgün istifadəçi adı daxil edin.', 'yanlışdır')], verbose_name='username'),
        ),
    ]

# Generated by Django 3.1.12 on 2021-06-15 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0002_auto_20210615_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenge.author', verbose_name='Author'),
        ),
    ]

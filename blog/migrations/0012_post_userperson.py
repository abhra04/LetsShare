# Generated by Django 3.1 on 2020-12-14 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20201214_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='userPerson',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.person'),
        ),
    ]
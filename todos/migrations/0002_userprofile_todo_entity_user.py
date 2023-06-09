# Generated by Django 4.2 on 2023-04-24 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='user', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='todo_entity',
            name='user',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, to='todos.userprofile'),
        ),
    ]

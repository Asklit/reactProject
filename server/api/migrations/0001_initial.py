# Generated by Django 5.1.3 on 2024-12-08 10:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('email', models.CharField(max_length=20, unique=True)),
                ('password_hash', models.CharField()),
                ('english_level', models.CharField(max_length=2)),
                ('is_email_verificated', models.BooleanField(default=False)),
                ('account_created_at', models.DateTimeField(auto_now_add=True)),
                ('password_changed_at', models.DateTimeField(auto_now=True)),
                ('last_day_online', models.DateTimeField(auto_now_add=True)),
                ('days_in_berserk', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id_word', models.AutoField(primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=30, unique=True)),
                ('translate_word', models.CharField(max_length=30)),
                ('word_level', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'Words',
            },
        ),
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('id_admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.users')),
                ('first_name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('established_post', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Admins',
            },
        ),
        migrations.CreateModel(
            name='LearnedWords',
            fields=[
                ('id_learned_word', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.users')),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.words')),
            ],
            options={
                'db_table': 'LearnedWords',
                'unique_together': {('word', 'user')},
            },
        ),
        migrations.CreateModel(
            name='WordsInProgress',
            fields=[
                ('id_word_in_progress', models.AutoField(primary_key=True, serialize=False)),
                ('number_views', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.users')),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.words')),
            ],
            options={
                'db_table': 'WordsInProgress',
                'unique_together': {('word', 'user')},
            },
        ),
    ]

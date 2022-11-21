# Generated by Django 4.1.3 on 2022-11-06 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trivia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('answer_one', models.CharField(max_length=200)),
                ('answer_two', models.CharField(max_length=200)),
                ('answer_three', models.CharField(max_length=200)),
                ('answer_four', models.CharField(max_length=200)),
                ('correct', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=50)),
            ],
        ),
    ]
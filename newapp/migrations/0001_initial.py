# Generated by Django 2.2.1 on 2019-05-23 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campus', models.CharField(help_text='Campus', max_length=20)),
                ('semester', models.CharField(help_text='Semester', max_length=20)),
                ('title', models.CharField(help_text='Title', max_length=20)),
                ('credit', models.CharField(help_text='Credit', max_length=20)),
                ('department', models.CharField(help_text='Department', max_length=20)),
                ('instructor', models.CharField(help_text='Instructor', max_length=20)),
                ('times', models.CharField(help_text='Times', max_length=20)),
                ('room', models.CharField(help_text='Times', max_length=20)),
                ('additional_info', models.CharField(help_text='Additional Info', max_length=20)),
                ('misc_links', models.CharField(help_text='Misc. Links', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(help_text='Username', max_length=30)),
                ('question', models.CharField(help_text='Question', max_length=140)),
                ('details', models.CharField(help_text='Question Details', max_length=3000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]

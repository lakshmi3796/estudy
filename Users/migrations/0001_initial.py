# Generated by Django 3.2.14 on 2022-07-16 11:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(help_text='Username of Student', max_length=256)),
                ('firstname', models.TextField(default='', help_text='First Name')),
                ('lastname', models.TextField(default='', help_text='Last Name')),
                ('email_id', models.TextField(default='', help_text='Email Id')),
                ('password', models.CharField(blank=True, help_text='Password of Student', max_length=256, null=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_login_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
    ]

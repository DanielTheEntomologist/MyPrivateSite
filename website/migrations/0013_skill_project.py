# Generated by Django 4.2.13 on 2024-10-14 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_curriculumvitae'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='')),
                ('hosted_url', models.URLField()),
                ('github_url', models.URLField()),
                ('skills', models.ManyToManyField(to='website.skill')),
            ],
        ),
    ]

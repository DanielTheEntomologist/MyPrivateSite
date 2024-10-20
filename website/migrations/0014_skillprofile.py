# Generated by Django 4.2.13 on 2024-10-14 20:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0013_skill_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('rating', models.IntegerField()),
                ('skills', models.ManyToManyField(to='website.skill')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

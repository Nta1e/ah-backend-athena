# Generated by Django 2.1.3 on 2018-12-12 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('body', models.TextField(db_index=True)),
                ('description', models.CharField(db_index=True, max_length=255, null=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('published', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='ArticleImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(blank=True, null=True)),
                ('description', models.CharField(db_index=True, max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.ArticleImg'),
        ),
    ]

# Generated by Django 4.2.9 on 2024-03-11 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('image_urls', models.JSONField(max_length=4095)),
                ('back_image_urls', models.JSONField(max_length=4095)),
                ('price_without_fee', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('stock', models.IntegerField(default=0)),
                ('description', models.CharField(blank=True, max_length=1023, null=True)),
                ('is_public', models.BooleanField(default=False)),
                ('logo_color', models.CharField(default=0, max_length=15)),
                ('is_new', models.BooleanField(default=False)),
                ('is_recommended', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

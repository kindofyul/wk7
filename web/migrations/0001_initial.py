# Generated by Django 4.2.1 on 2023-05-15 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('r_rate', models.FloatField()),
                ('status', models.BooleanField(default=False)),
                ('review', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='movie/')),
            ],
        ),
    ]

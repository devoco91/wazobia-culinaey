# Generated by Django 5.1.3 on 2025-01-31 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=15)),
                ('course', models.CharField(choices=[('1', 'Basic (200,000 Naira)'), ('2', 'Intensive (300,000 Naira)'), ('3', 'Advanced (400,000 Naira)')], max_length=50)),
                ('mode_of_study', models.CharField(choices=[('Weekday', 'Weekday'), ('Weekend', 'Weekend')], max_length=10)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Prefer not to say', 'Prefer not to say')], max_length=20)),
                ('shirt_size', models.CharField(choices=[('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=5)),
                ('agree', models.BooleanField(default=False)),
            ],
        ),
    ]

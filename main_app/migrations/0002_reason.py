# Generated by Django 3.2.12 on 2022-09-15 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.shoe')),
            ],
        ),
    ]

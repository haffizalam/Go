# Generated by Django 2.1.7 on 2021-06-01 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(blank=True, upload_to='product_image')),
                ('faname', models.CharField(max_length=50)),
                ('mname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('mstatus', models.CharField(max_length=20)),
                ('height', models.CharField(max_length=10)),
                ('profession', models.CharField(max_length=50)),
                ('qualification', models.CharField(max_length=50)),
                ('religion', models.CharField(max_length=50)),
                ('mothertongue', models.CharField(max_length=50)),
                ('cityname', models.CharField(max_length=50)),
                ('dist', models.CharField(max_length=50)),
                ('pin', models.CharField(max_length=10)),
                ('hobbies', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

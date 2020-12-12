# Generated by Django 3.1.4 on 2020-12-12 14:57

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
            name='BlockChain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('salt', models.BinaryField()),
                ('iv', models.BinaryField()),
                ('file_password', models.CharField(max_length=256)),
                ('cipher_text', models.BinaryField()),
                ('previous_hash', models.CharField(blank=True, max_length=64)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_blocks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=256)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_block', to='blockchain.blockchain')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_files', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

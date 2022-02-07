# Generated by Django 3.2.11 on 2022-02-07 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0010_alter_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='IconSocialNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icon')),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='icon_social_network', to='perfil.network')),
            ],
        ),
    ]

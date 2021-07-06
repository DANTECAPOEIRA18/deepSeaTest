# Generated by Django 3.2.5 on 2021-07-06 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='teams',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_team', models.CharField(max_length=250)),
                ('date_create', models.DateField(auto_now=True, verbose_name='Date Create')),
                ('image_team', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_b64', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Teams',
                'verbose_name_plural': 'Team',
                'ordering': ['name_team'],
            },
        ),
    ]

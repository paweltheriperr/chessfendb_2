# Generated by Django 4.2.5 on 2023-09-21 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fen', models.TextField(blank=True)),
                ('user', models.CharField(blank=True, max_length=50)),
                ('debiut_name', models.CharField(max_length=255, null=True)),
                ('added', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Fen',
                'verbose_name_plural': "Fen's",
                'ordering': ['pk'],
            },
        ),
    ]
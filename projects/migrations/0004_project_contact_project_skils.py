# Generated by Django 4.0.2 on 2022-03-14 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_qualification'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='contact',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='skils',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]

# Generated by Django 4.0 on 2021-12-18 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='major',
            field=models.CharField(choices=[('CS', 'Computer Science'), ('BIO', 'Biology')], max_length=250, null=True),
        ),
    ]

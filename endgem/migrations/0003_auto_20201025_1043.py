# Generated by Django 3.1.2 on 2020-10-25 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endgem', '0002_auto_20201025_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
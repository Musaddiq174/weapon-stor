# Generated by Django 5.1 on 2024-09-09 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_shop_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='name',
        ),
        migrations.AddField(
            model_name='shop',
            name='name1',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

# Generated by Django 5.1 on 2024-09-09 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_shop_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

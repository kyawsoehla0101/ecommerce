# Generated by Django 4.2.4 on 2023-09-01 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
    ]

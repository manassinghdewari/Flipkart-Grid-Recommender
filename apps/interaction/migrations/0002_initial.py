# Generated by Django 4.2.2 on 2023-08-21 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('interaction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='interaction',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]

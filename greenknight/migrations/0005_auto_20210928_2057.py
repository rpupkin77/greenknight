# Generated by Django 3.1.4 on 2021-09-28 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('greenknight', '0004_auto_20210119_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cart_key',
            field=models.CharField(db_index=True, max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='greenknight.cart'),
        ),
    ]

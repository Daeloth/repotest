# Generated by Django 4.0.4 on 2022-06-28 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manguera', '0006_cliente_alter_item_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='edad',
        ),
        migrations.AddField(
            model_name='cliente',
            name='correo',
            field=models.EmailField(default='pene@pene.pene', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(default='peneeeee', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='fono',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='rut',
            field=models.CharField(default=0, max_length=9),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.1.5 on 2019-02-16 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='ativado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='domingo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='key',
            field=models.CharField(max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='quarta',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='quinta',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='sabado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='segunda',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='sexta',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='terca',
            field=models.BooleanField(default=True),
        ),
    ]

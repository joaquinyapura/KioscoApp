# Generated by Django 4.2 on 2023-05-20 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50)),
                ('contra', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='telefono',
            field=models.IntegerField(),
        ),
    ]
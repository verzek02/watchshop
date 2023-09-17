# Generated by Django 4.2.5 on 2023-09-17 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='watch',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='watch',
            name='image',
            field=models.ImageField(null=True, upload_to='watches'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='category',
            field=models.CharField(choices=[('Спортивные', 'Спортивные'), ('классическое', 'Классическое'), ('Детское', 'Детское')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='watch',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='watch',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='watch',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
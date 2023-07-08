# Generated by Django 4.2 on 2023-06-25 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_card_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.CharField(default='images/placeholder.webp', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(default='Player', max_length=50),
        ),
    ]
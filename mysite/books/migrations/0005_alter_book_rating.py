# Generated by Django 5.0.6 on 2024-07-01 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_price_alter_book_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=2),
        ),
    ]

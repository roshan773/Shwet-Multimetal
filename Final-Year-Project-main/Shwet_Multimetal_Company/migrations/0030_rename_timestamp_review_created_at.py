# Generated by Django 5.0.3 on 2024-04-16 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shwet_Multimetal_Company', '0029_remove_order_product_remove_order_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='timeStamp',
            new_name='created_at',
        ),
    ]

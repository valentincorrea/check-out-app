# Generated by Django 4.1.7 on 2023-03-26 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptoprequest', '0013_alter_computer_computer_classification_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='returned',
            field=models.BooleanField(default=False, verbose_name='Returned'),
        ),
        migrations.AddField(
            model_name='request',
            name='returned_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='order_status',
            field=models.CharField(choices=[('Created', 'Created'), ('Pending', 'Pending'), ('Processing', 'Processing'), ('Ready', 'Ready'), ('Rejected', 'Check Out'), ('Returned', 'Returned')], default='Created', max_length=10),
        ),
    ]
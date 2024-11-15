# Generated by Django 5.1.3 on 2024-11-15 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('Customer_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Customer_name', models.CharField(max_length=100)),
                ('Mobile_no', models.IntegerField()),
                ('Age', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('DoB', models.DateField()),
                ('Loan_amount', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Electricity_Bill',
        ),
    ]
# Generated by Django 4.1.7 on 2023-03-28 13:22

from django.db import migrations, models
import django.db.models.deletion
import fi.models


class Migration(migrations.Migration):

    dependencies = [
        ('fi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fi.transactioncategory')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('type', models.CharField(default='E', max_length=1, validators=[fi.models.transaction_type_validate])),
                ('amount', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='fi.transactioncategory')),
            ],
        ),
    ]

# Generated by Django 3.2.7 on 2021-09-08 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Category name', max_length=100, unique=True, verbose_name='category name')),
                ('description', models.CharField(blank=True, help_text='Description category', max_length=200, null=True, verbose_name='Description category')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='OrderRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Order name', max_length=100, unique=True, verbose_name='order name')),
                ('description', models.CharField(blank=True, help_text='Description order request', max_length=200, null=True, verbose_name='Description order')),
            ],
            options={
                'verbose_name': 'order_request',
                'verbose_name_plural': 'order_requests',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time at which an object was created', verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time at which an object was modified', verbose_name='updated_at')),
                ('name', models.CharField(max_length=100, verbose_name='Product name')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Description product')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('quantity', models.PositiveIntegerField()),
                ('category_id', models.ForeignKey(blank=True, db_column='category_id', null=True, on_delete=django.db.models.deletion.RESTRICT, to='Acme.category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
        migrations.CreateModel(
            name='OperationDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time at which an object was created', verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time at which an object was modified', verbose_name='updated_at')),
                ('quantity_total', models.IntegerField(help_text='Items sold/bought', verbose_name='Total quantity')),
                ('total_charge', models.DecimalField(decimal_places=2, help_text='Total amount of movement', max_digits=9, verbose_name='Total charge')),
                ('category_id', models.ForeignKey(blank=True, db_column='category_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Acme.category')),
                ('product_id', models.ForeignKey(blank=True, db_column='product_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Acme.product')),
                ('type_operation_id', models.ForeignKey(blank=True, db_column='type_operation_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Acme.orderrequest')),
            ],
            options={
                'verbose_name': 'operation_details',
                'verbose_name_plural': 'detail_operations',
            },
        ),
    ]

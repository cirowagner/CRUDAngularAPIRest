# Generated by Django 3.2.8 on 2021-10-05 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kardex', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=8)),
                ('nombre', models.CharField(max_length=50)),
                ('ruc', models.CharField(max_length=10)),
                ('razon', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=70)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Comprobante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tcomprobante', models.CharField(choices=[('FACTURA', 'FACTURA'), ('BOLETA', 'BOLETA DE VENTA'), ('GUIA', 'GUIA DE REMISION'), ('OTROS', 'OTROS')], max_length=20)),
                ('numfactura', models.CharField(max_length=10)),
                ('numboleta', models.CharField(max_length=10)),
                ('fecha', models.DateField()),
                ('igv', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.cliente')),
            ],
            options={
                'verbose_name': 'Comprobante',
                'verbose_name_plural': 'Comprobantes',
            },
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('importe', models.FloatField()),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('comprobante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.comprobante')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kardex.producto')),
            ],
            options={
                'verbose_name': 'Detalle',
                'verbose_name_plural': 'Detalles',
            },
        ),
    ]

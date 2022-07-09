# Generated by Django 4.0.4 on 2022-05-11 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Date1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Ratio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Historic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portafolioVirtual.company')),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portafolioVirtual.date1')),
            ],
        ),
    ]

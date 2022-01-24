# Generated by Django 3.2 on 2022-01-24 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220119_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('plan_length', models.CharField(max_length=50)),
                ('difficulty', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('days_per_week', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('description', models.TextField()),
                ('Equipment', models.CharField(max_length=254)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
            ],
        ),
    ]

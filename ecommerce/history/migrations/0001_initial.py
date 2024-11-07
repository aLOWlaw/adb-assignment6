# Generated by Django 4.1.13 on 2024-11-07 17:01

from django.db import migrations, models
import djongo.models.fields
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryModel',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('product', djongo.models.fields.EmbeddedField(model_container=products.models.ProductsModel)),
                ('user', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('iteraction', models.CharField(choices=[('like', 'like'), ('purchase', 'purchase')], max_length=128)),
            ],
        ),
    ]

# Generated by Django 4.2 on 2023-04-27 20:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quotes_list", "0004_alter_authors_description_alter_quotes_quote"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

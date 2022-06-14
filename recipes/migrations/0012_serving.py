# Generated by Django 4.0.3 on 2022-06-10 16:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_alter_shoppingitem_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='Serving',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servings', to='recipes.recipe')),
            ],
        ),
    ]
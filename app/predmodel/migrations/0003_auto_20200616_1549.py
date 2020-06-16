# Generated by Django 3.0.7 on 2020-06-16 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('predmodel', '0002_remove_predmodel_species_included'),
    ]

    operations = [
        migrations.RenameField(
            model_name='predmodel',
            old_name='date_added',
            new_name='created_date',
        ),
        migrations.AddField(
            model_name='predmodel',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]

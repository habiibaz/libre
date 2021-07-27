# Generated by Django 3.1.7 on 2021-07-27 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0024_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.projectlist'),
        ),
        migrations.AlterField(
            model_name='report',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.servicelist'),
        ),
    ]
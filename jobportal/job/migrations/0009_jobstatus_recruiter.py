# Generated by Django 4.1.3 on 2022-11-26 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_remove_apply_status_jobstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobstatus',
            name='recruiter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='job.recruiter'),
        ),
    ]

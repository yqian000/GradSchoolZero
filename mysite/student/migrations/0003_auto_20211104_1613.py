# Generated by Django 3.2.9 on 2021-11-04 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_rename_transcript_applcation_transcprit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applcation',
            name='letters',
            field=models.FileField(upload_to='student/documents/'),
        ),
        migrations.AlterField(
            model_name='applcation',
            name='personal_statement',
            field=models.FileField(upload_to='student/documents/'),
        ),
        migrations.AlterField(
            model_name='applcation',
            name='transcprit',
            field=models.FileField(upload_to='student/documents/'),
        ),
    ]

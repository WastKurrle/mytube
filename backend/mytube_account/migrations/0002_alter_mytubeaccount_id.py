# Generated by Django 4.1.7 on 2023-03-26 20:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mytube_account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytubeaccount',
            name='id',
            field=models.CharField(default=uuid.UUID('7e67b592-4924-4161-884d-53465b9c7e1a'), editable=False, max_length=255, primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 4.1.7 on 2023-05-19 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytube_account', '0003_alter_mytubeaccount_id'),
        ('video', '0006_alter_video_dislikes_alter_video_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='disliked_videos', to='mytube_account.mytubeaccount'),
        ),
        migrations.AlterField(
            model_name='video',
            name='likes',
            field=models.ManyToManyField(related_name='liked_videos', to='mytube_account.mytubeaccount'),
        ),
    ]

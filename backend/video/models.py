from django.db import models
from django.utils import timezone
from mytube_account.models import MyTubeAccount
from users.models import User
from mytube import settings


class Video(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=255)
    name = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos/')
    description = models.TextField(null=True)
    thumbnail = models.ImageField(upload_to='videos-thumbnails/')
    datetime_posted = models.DateTimeField(default=timezone.now)
    calls = models.PositiveIntegerField(default=0)
    mt_account = models.ForeignKey(MyTubeAccount, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if settings.DEBUG:
            return f'http://localhost:5173/video/{self.id}'

        return f'https://mytube.sebastiankurrle-projects.de/video/{self.id}'

    def get_video(self):
        if settings.DEBUG:
            return f'http://127.0.0.1:8000{self.video.url}'

        return f'http://apimt.sebastiankurrle-projects.de{self.video.url}'

    def get_thumbnail(self):
        if settings.DEBUG:
            return f'http://127.0.0.1:8000{self.thumbnail.url}'

        return f'https://apimt.sebastiankurrle-projects.de{self.thumbnail.url}'


class Evaluate(models.Model):
    EVALUATE_CHOICES = (
        (0, 'like'),
        (1, 'dislike')
    )

    id = models.CharField(primary_key=True, editable=False, max_length=255)
    evaluate = models.CharField(choices=EVALUATE_CHOICES, max_length=255)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Comment(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=255)
    message = models.TextField()
    datetime_posted = models.DateTimeField(default=timezone.now)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

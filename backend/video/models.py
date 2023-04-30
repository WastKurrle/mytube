from django.db import models
from mytube_account.models import MyTubeAccount


class Video(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    thumbnail = models.ImageField(upload_to='videos/')
    mt_account = models.ForeignKey(MyTubeAccount, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'http://localhost:5173/{self.id}'

    def get_thumbnail(self):
        return f'http://127.0.0.1:8000/{self.thumbnail.url}'

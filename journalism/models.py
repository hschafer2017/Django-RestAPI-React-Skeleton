from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    content = models.TextField(blank=False)
    image = models.ImageField(upload_to='images', null=False)
    published_date = models.DateTimeField(blank=True, null=True,
                                          default=timezone.now)

    def __str__(self):
        return self.title

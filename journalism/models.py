from django.db import models
from django.utils import timezone


class Publication(models.Model):
    name = models.CharField(max_length=100, blank=False,
                            null=False)
    affiliation = models.CharField(max_length=100, blank=False,
                                   null=False)
    city = models.CharField(max_length=100,
                            blank=False,
                            null=False)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    content = models.TextField(blank=False)
    image = models.ImageField(upload_to='images', null=False)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    publication = models.ForeignKey('Publication',
                                    on_delete=models.CASCADE,
                                    related_name='articles')
    class Meta:
        unique_together = ('publication', 'title')
        ordering = ['publication']

    def __unicode__(self):
        return '%d: %s' % (self.publication, self.title)

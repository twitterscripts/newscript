from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class BugReport(models.Model):
    authorr = models.CharField(max_length=20)
    titler = models.CharField(max_length=200)
    textr = models.TextField()
    created_dater = models.DateTimeField(default=timezone.now)
    published_dater = models.DateTimeField(blank=True, null=True)

    def publishr(self):
        self.published_dater = timezone.now()
        self.save()

    def __str__(self):
        return self.titler
from django.db import models


class Team(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    fb_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    linkedIn_link = models.URLField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)



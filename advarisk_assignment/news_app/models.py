from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Keyword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phrase = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    last_search_time = models.DateTimeField(auto_now=True)

class SearchResult(models.Model):
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.URLField()
    date_published = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
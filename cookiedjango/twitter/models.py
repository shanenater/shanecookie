from django.db import models
from cookiedjango.core.models import TimeStampedModel

class TwitterPost(TimeStampedModel):
    tag = models.CharField(max_length=140)
    text = models.TextField()

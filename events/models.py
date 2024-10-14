from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))
EVENTTYPE = ((0, "MudRun"), (1, "Hiking"), (2, "Other"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=False)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="events_posts"
    )
    date = models.DateField()
    eventtype = models.IntegerField(choices=EVENTTYPE, default=0)
    location = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
from django.db import models


# Create your models here.
class Post(models.Model):
    """ A model to render the Pagedown Markdown """
    title = models.CharField(max_length=300)
    post_field = models.TextField(blank=True)

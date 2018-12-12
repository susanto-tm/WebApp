from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Post(models.Model):
    """ A model to render the Pagedown Markdown """
    title = models.CharField(max_length=300)
    post_field = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

# class Post_Forum(models.Model):
#     """A model to render the information from Post Model"""
#     title = models.CharField()
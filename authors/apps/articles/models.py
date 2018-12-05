from datetime import datetime, timedelta
from ..authentication.models import User
from django.db import models


class ArticleImg(models.Model):
    image = models.CharField(null=True, max_length=255, blank=True)
    description = models.CharField(db_index=True, max_length=255)


class Article(models.Model):
    """
    This class implements an article model,the author field
    identifies an article with a certain user.
    """

    """Every modle a title ield"""
    tittle = models.CharField(db_index=True, max_length=255)

    """The author field identifies an article with a certain user."""
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    """The body field is the actual body of the article."""
    body = models.TextField(db_index=True)

    """An article can have images in the body"""
    image = models.ForeignKey(ArticleImgs, on_delete=models.CASCADE)

    """A description contains what the article is about"""
    description = models.CharField(db_index=True, max_length=255)

    """. The slug field makes the article searchable it can be 
    auto generated or specified by the author."""
    slug = models.SlugField(db_index=True, max_length=255, unique=True)

    """
    Published is like a draft field, helps authors to wor
    and save them to draft before publishing them
    """
    published = models.BooleanField(default=False)

    """
    created at and updated at fiedls track the authors
    edit history of the article
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.tittle

    class Meta:
        ordering = ["-created_at", "-updated_at"]
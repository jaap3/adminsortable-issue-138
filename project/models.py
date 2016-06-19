from adminsortable.models import SortableMixin
from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=40)
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title


class Track(SortableMixin):
    album = models.ForeignKey(Album)
    position = models.PositiveSmallIntegerField(default=1, editable=False, db_index=True)
    artist = models.CharField(max_length=40)
    title = models.CharField(max_length=40)
    duration = models.CharField(max_length=40)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.title

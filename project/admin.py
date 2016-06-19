from django.contrib import admin

from adminsortable.admin import NonSortableParentAdmin, SortableStackedInline

from .models import Track, Album


class TrackInline(SortableStackedInline):
    model = Track


@admin.register(Album)
class AlbumAdmin(NonSortableParentAdmin):
    inlines = [TrackInline]

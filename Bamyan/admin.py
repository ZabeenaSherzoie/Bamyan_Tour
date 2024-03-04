from django.contrib import admin
from .models import TourAgency, Season, Package
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


@admin.register(TourAgency)
class TourAgencyAdmin(SummernoteModelAdmin):
    summernote_fields = ('description')


@admin.register(Package)
class PackageAdmin(SummernoteModelAdmin):
    list_display = ('title', 'duration', 'package_size')
    search_fields = ('title', 'season')
    list_filter = ('season',)
    summernote_fields = ('description')


@admin.register(Season)
class SeasonAdmin(SummernoteModelAdmin):
    summernote_fields = ('description')


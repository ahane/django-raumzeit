from django.contrib import admin
from happenings.models import Happening, HappeningLink, ThirdParty, Location, Artist, Performance, LocationLink, ArtistLink
admin.site.register([HappeningLink, ThirdParty, Location, Performance, Artist, LocationLink, ArtistLink])

# Register your models here.

class PerformanceInline(admin.TabularInline):
    model = Performance

class HappeningAdmin(admin.ModelAdmin):
    inlines = (PerformanceInline, )




admin.site.register(Happening, HappeningAdmin)

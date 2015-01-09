from django.contrib import admin
from happenings.models import Happening, HappeningLink, ThirdParty, Location, Artist, Performance
admin.site.register([Happening, HappeningLink, ThirdParty, Location, Artist, Performance])
# Register your models here.

from django.contrib import admin
from happenings.models import Happening, HappeningLink, ThirdParty, Location
admin.site.register([Happening, HappeningLink, ThirdParty, Location])
# Register your models here.

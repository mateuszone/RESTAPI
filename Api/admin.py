from django.contrib import admin
# Register your models here.
from Api.models import Film, ExtraInfo, Review, Actor

admin.site.register(Film)
admin.site.register(ExtraInfo)
admin.site.register(Review)
admin.site.register(Actor)
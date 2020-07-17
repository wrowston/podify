from django.contrib import admin
from .models import Episode, Creator, Podcast

# Register your models here.

admin.site.register([Episode, Creator, Podcast])

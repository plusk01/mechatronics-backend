from django.contrib import admin
from api.models import *

# Register your models here.
admin.site.register(Member)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(HackNight)
admin.site.register(HackNightResource)
admin.site.register(Announcement)
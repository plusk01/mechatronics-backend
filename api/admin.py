from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.conf import settings
from api.models import *

# Make the Custom User have the password change field, etc
class MemberChangeForm(UserChangeForm):
	class Meta(UserChangeForm.Meta):
		model = get_user_model()


class MemberAdmin(UserAdmin):
    form = MemberChangeForm

    # fieldsets = UserAdmin.fieldsets + (
    #         (None, {'fields': ('some_extra_data',)}),
    # )


# Register your models here.
admin.site.register(Member, MemberAdmin)
admin.site.register(FieldOfStudy)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(HackNight)
admin.site.register(HackNightResource)
admin.site.register(Announcement)
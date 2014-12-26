from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create your models here.
class Member(AbstractUser):
    projects = models.ManyToManyField('Project', null=True, blank=True)
    skills = models.ManyToManyField('Skill', null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profiles', null=True, blank=True)
    paid = models.NullBooleanField()
    presenter = models.NullBooleanField()
    honorary = models.NullBooleanField()

    def __unicode__(self):
        return "[{}]: {}".format(self.id, self.username)

class Skill(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return "[{}]: {}".format(self.id, self.name)

class Project(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	date_started = models.DateField(auto_now_add=True)
	date_completed = models.DateField(blank=True, null=True)
	competition = models.NullBooleanField()

	def __unicode__(self):
		return "[{}]: {}".format(self.id, self.name)

class HackNight(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	date = models.DateField()
	repo = models.CharField(max_length=100, null=True, blank=True)
	presenter = models.ForeignKey(Member, related_name='presentations')
	tags = models.CharField(max_length=300)

	def __unicode__(self):
		return "[{}]: '{}' by {}".format(self.id, self.title, self.presenter.username)


class HackNightResource(models.Model):
	presentation = models.ForeignKey(HackNight, related_name='resources')
	file = models.FileField(upload_to='resources')
	uploaded = models.DateTimeField(auto_now_add=True)
	uploader = models.ForeignKey(Member, related_name='uploads')

	def __unicode__(self):
		return "[{}]: {}".format(self.id, self.presentation.title)

class Announcement(models.Model):
	title = models.CharField(max_length=100)
	short_description = models.CharField(max_length=255)
	long_description = models.TextField(null=True, blank=True)
	created = models.DateField(auto_now_add=True)
	creator = models.ForeignKey(Member, related_name='announcements')

	def __unicode__(self):
		return "[{}]: {}".format(self.id, self.title)
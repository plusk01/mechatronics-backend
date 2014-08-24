from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User, related_name='member_info')
    projects = models.ManyToManyField('Project')
    skills = models.ManyToManyField('Skill')
    profile_picture = models.ImageField(upload_to='profiles')
    paid = models.NullBooleanField()
    presenter = models.NullBooleanField()
    honorary = models.NullBooleanField()

    def __unicode__(self):
        pass

class Skill(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		pass

class Project(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	date_started = models.DateField(auto_now_add=True)
	date_completed = models.DateField(blank=True, null=True)
	competition = models.NullBooleanField()

	def __unicode__(self):
		pass

class HackNight(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	date = models.DateField()
	presenter = models.ForeignKey(Member, related_name='presentations')
	tags = models.ManyToManyField('Tag', related_name='presentations')

	def __unicode__(self):
		pass

class Tag(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		pass

class HackNightResource(models.Model):
	presentation = models.ForeignKey(HackNight, related_name='resources')
	file = models.FileField(upload_to='resources')
	uploaded = models.DateTimeField(auto_now_add=True)
	uploader = models.ForeignKey(Member, related_name='uploads')

	def __unicode__(self):
		pass

class Announcement(models.Model):
	title = models.CharField(max_length=100)
	short_description = models.CharField(max_length=255)
	long_description = models.TextField(null=True, blank=True)
	created = models.DateField(auto_now_add=True)
	creator = models.ForeignKey(Member, related_name='announcements')

	def __unicode__(self):
		pass
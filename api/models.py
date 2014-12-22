from django.db import models
from django.contrib.auth.models import AbstractUser

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
	presenter = models.ForeignKey(Member, related_name='presentations')
	tags = models.ManyToManyField('Tag', related_name='presentations')

	def __unicode__(self):
		return "[{}]: '{}' by {}".format(self.id, self.title, self.presenter.username)

class Tag(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return "[{}]: {}".format(self.id, self.name)

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
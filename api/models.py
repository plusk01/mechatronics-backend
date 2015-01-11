from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import UserManager
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from rest_framework.authtoken.models import Token

import datetime
import mailchimp

from api.managers import MemberObjectsManager, MemberManager

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def subscribe_member(sender, instance=None, created=False, **kwargs):
	if created:
		try:
			m = mailchimp.Mailchimp(settings.MAILCHIMP_APIKEY)
			m.lists.subscribe(settings.MAILCHIMP_LISTID, {
					'email': instance.email,
				},
				merge_vars={
					'FNAME': instance.first_name,
					'LNAME': instance.last_name,
				}, double_optin=False)
		except:
			pass

# Create your models here.
class FieldOfStudy(models.Model):
	name = models.CharField(max_length=255)

	def __unicode__(self):
		return "[{}]: {}".format(self.id, self.name)


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


class Member(AbstractBaseUser, PermissionsMixin):
	first_name = models.CharField(max_length=30, blank=True)
	last_name = models.CharField(max_length=30, blank=True)
	email = models.EmailField(max_length=255, unique=True, verbose_name='email address')
	is_staff = models.BooleanField(default=False,
	    help_text='Designates whether the user can log into this admin site.')
	is_active = models.BooleanField(default=True,
	    help_text='Designates whether this user should be treated as active. '
	    	'Unselect this instead of deleting accounts.')
	date_joined = models.DateTimeField(default=timezone.now)

	grad_year = models.IntegerField(default=0)
	major = models.ForeignKey(FieldOfStudy, null=True, blank=True, related_name='major_members')
	minor = models.ForeignKey(FieldOfStudy, null=True, blank=True, related_name='minor_members')
	projects = models.ManyToManyField(Project, null=True, blank=True)
	skills = models.ManyToManyField(Skill, null=True, blank=True)
	profile_picture = models.ImageField(upload_to='profiles', null=True, blank=True)
	paid = models.NullBooleanField()
	presenter = models.NullBooleanField()
	honorary = models.NullBooleanField()

	# For the API
	token_only = models.BooleanField(default=False,
		help_text='Indicates that this isn\'t a real member, but only an API token.')

	# Managers
	objects = MemberObjectsManager()
	members = MemberManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	class Meta:
		verbose_name = 'member'
		verbose_name_plural = 'members'

	def __unicode__(self):
		return "[{}]: {}".format(self.id, self.email)

	def get_full_name(self):
	    """
	    Returns the first_name plus the last_name, with a space in between.
	    """
	    full_name = '%s %s' % (self.first_name, self.last_name)
	    return full_name.strip()

	def get_short_name(self):
	    "Returns the short name for the user."
	    return self.first_name

	def email_user(self, subject, message, from_email=None, **kwargs):
	    """
	    Sends an email to this User.
	    """
	    send_mail(subject, message, from_email, [self.email], **kwargs)


class HackNight(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	date = models.DateField()
	repo = models.CharField(max_length=100, null=True, blank=True)
	presenter = models.ForeignKey(Member, related_name='presentations')
	tags = models.CharField(max_length=300)

	def __unicode__(self):
		return "[{}]: '{}' by {}".format(self.id, self.title, self.presenter.email)


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
	date = models.DateField(default=datetime.date.today)
	creator = models.ForeignKey(Member, related_name='announcements')

	def __unicode__(self):
		return "[{}]: {}".format(self.id, self.title)
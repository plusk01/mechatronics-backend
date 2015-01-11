from django.contrib.auth.models import BaseUserManager
from django.db import models

import datetime

class MemberObjectsManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class MemberManager(MemberObjectsManager):
	def get_queryset(self):
		return super(MemberManager, self).get_queryset().filter(token_only=False)


class AnnouncementManager(models.Manager):
    def get_queryset(self):
        ANNOUNCEMENT_SHOW_RECENT = 3
        start_date = datetime.datetime.now() - datetime.timedelta(days=ANNOUNCEMENT_SHOW_RECENT)
        return super(AnnouncementManager, self).get_queryset().filter(date__gte=start_date.date()).order_by('date')
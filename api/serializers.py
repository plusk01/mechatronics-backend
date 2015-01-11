from rest_framework import serializers
from django.conf import settings

from api.models import *


class MemberSerializer(serializers.ModelSerializer):
	full_name = serializers.SerializerMethodField('_full_name')
	major = serializers.SerializerMethodField('_major')
	minor = serializers.SerializerMethodField('_minor')

	class Meta:
		exclude = ['password', 'user_permissions']
		model = Member

	def _full_name(self, obj):
		return "{} {}".format(obj.first_name, obj.last_name)

	def _major(self, obj):
		if obj.major:
			return FieldOfStudySerializer(obj.major).data

		return None

	def _minor(self, obj):
		if obj.minor:
			return FieldOfStudySerializer(obj.minor).data

		return None


class SkillSerializer(serializers.ModelSerializer):
	class Meta:
		model = Skill


class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project


class HackNightSerializer(serializers.ModelSerializer):
	presenter = serializers.SerializerMethodField('_presenter')
	repo = serializers.SerializerMethodField('_repo')
	tags = serializers.SerializerMethodField('_tags')

	class Meta:
		model = HackNight

	def _presenter(self, obj):
		return MemberSerializer(obj.presenter, context=self.context).data

	def _repo(self, obj):
		if obj.repo:
			return "{}/{}".format(settings.GITHUB_ROOT, obj.repo)

		return None

	def _tags(self, obj):
		tagList = obj.tags.split(',')
		return [tag.strip() for tag in tagList]


class HackNightResourceSerializer(serializers.ModelSerializer):
	class Meta:
		model = HackNightSerializer


class AnnouncementSerializer(serializers.ModelSerializer):
	day = serializers.SerializerMethodField('_day')
	month = serializers.SerializerMethodField('_month')

	class Meta:
		model = Announcement

	def _day(self, obj):
		return "{}".format(obj.date.strftime("%d"))

	def _month(self, obj):
		return "{}".format(obj.date.strftime("%B"))


class FieldOfStudySerializer(serializers.ModelSerializer):
	class Meta:
		model = FieldOfStudy		
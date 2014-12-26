from rest_framework import serializers
from django.conf import settings

from api.models import *


class MemberSerializer(serializers.ModelSerializer):
	full_name = serializers.SerializerMethodField('_full_name')

	class Meta:
		exclude = ['password', 'user_permissions']
		model = Member

	def _full_name(self, obj):
		return "{} {}".format(obj.first_name, obj.last_name)


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
		return MemberSerializer(obj.presenter).data

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
	class Meta:
		model = Announcement

		
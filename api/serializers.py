from rest_framework import serializers

from api.models import *
from django.contrib.auth.models import User


class MemberSerializer(serializers.ModelSerializer):
	class Meta:
		model = Member


class SkillSerializer(serializers.ModelSerializer):
	class Meta:
		model = Skill


class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project


class HackNightSerializer(serializers.ModelSerializer):
	class Meta:
		model = HackNight


class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag


class HackNightResourceSerializer(serializers.ModelSerializer):
	class Meta:
		model = HackNightSerializer


class AnnouncementSerializer(serializers.ModelSerializer):
	class Meta:
		model = Announcement

		
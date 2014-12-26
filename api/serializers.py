from rest_framework import serializers

from api.models import *


class MemberSerializer(serializers.ModelSerializer):
	full_name = serializers.SerializerMethodField('_full_name')

	class Meta:
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
	class Meta:
		model = HackNight


class HackNightResourceSerializer(serializers.ModelSerializer):
	class Meta:
		model = HackNightSerializer


class AnnouncementSerializer(serializers.ModelSerializer):
	class Meta:
		model = Announcement

		
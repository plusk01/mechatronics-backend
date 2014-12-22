from rest_framework import generics, permissions, viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from api.models import *
from api.serializers import *

# Create your views here.
class MemberViewSet(viewsets.ModelViewSet):
	queryset = Member.objects.all()
	serializer_class = MemberSerializer


class SkillViewSet(viewsets.ModelViewSet):
	queryset = Skill.objects.all()
	serializer_class = SkillSerializer


class ProjectViewSet(viewsets.ModelViewSet):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer


class HackNightViewSet(viewsets.ModelViewSet):
	queryset = HackNight.objects.all()
	serializer_class = HackNightSerializer


class TagViewSet(viewsets.ModelViewSet):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer


class HackNightResourceViewSet(viewsets.ModelViewSet):
	queryset = HackNightResource.objects.all()
	serializer_class = HackNightResourceSerializer


class AnnouncementViewSet(viewsets.ModelViewSet):
	queryset = Announcement.objects.all()
	serializer_class = AnnouncementSerializer
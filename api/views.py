from django.conf import settings
from django.core.mail import send_mail

from rest_framework import generics, permissions, viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from api.models import *
from api.serializers import *

# Create your views here.
class MemberViewSet(viewsets.ModelViewSet):
	queryset = Member.members.all()
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


class HackNightResourceViewSet(viewsets.ModelViewSet):
	queryset = HackNightResource.objects.all()
	serializer_class = HackNightResourceSerializer


class AnnouncementViewSet(viewsets.ModelViewSet):
	queryset = Announcement.objects.all()
	serializer_class = AnnouncementSerializer


class FieldOfStudyViewSet(viewsets.ModelViewSet):
	queryset = FieldOfStudy.objects.all()
	serializer_class = FieldOfStudySerializer


@api_view(('POST',))
def contact_view(request):
	# Build the message
	msg = "Name: {}\nEmail: {}\nMessage: {}".format(
			request.DATA['name'], request.DATA['email'], request.DATA['message']
		)

	# Send it away!
	sent = send_mail("[Mechatronics] Contact from {}".format(request.DATA['name']), \
			msg, settings.MAILTO, [settings.MAILTO]
		)

	if (sent == 1):
		return Response('Email sent', status=status.HTTP_200_OK)

	return Response('Oops', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
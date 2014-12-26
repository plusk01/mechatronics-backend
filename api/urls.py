from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r'members', views.MemberViewSet)
router.register(r'skills', views.SkillViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'hack-nights', views.HackNightViewSet)
router.register(r'hack-night-resources', views.HackNightResourceViewSet)
router.register(r'announcements', views.AnnouncementViewSet)



urlpatterns = patterns('',
	url(r'^', include(router.urls)),

	#url(r'^questions$', views.QuestionList.as_view(), name='question-list'),

)

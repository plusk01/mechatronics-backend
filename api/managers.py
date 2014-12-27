from django.contrib.auth.models import UserManager

class MemberManager(UserManager):
	def get_queryset(self):
		return super(MemberManager, self).get_queryset().filter(token_only=False)
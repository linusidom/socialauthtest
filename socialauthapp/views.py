from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from allauth.socialaccount.models import SocialAccount
class IndexTemplateView(TemplateView):
	template_name='index.html'

	def get_context_data(self):
		context = {
			'data':SocialAccount.objects.all()
			}
		
		return context
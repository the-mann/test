# Create your views here.
from allauth.socialaccount.models import SocialAccount
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, *args, **kwargs):
        x = super(Index, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated and 'extra_data' in user:
            username = user.username
            x['extra_data'] = SocialAccount.objects.filter(user=self.request.user)[0].extra_data
        else:
            username = "Not logged in"

        x['username'] = username
        x['user'] = self.request.user
        return x

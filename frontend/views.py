from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from properties.models import Property


# Create your views here.

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'account_login'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        properties = Property.objects.filter(is_active=True)
        context.update({
            'properties': properties,
        })
        return context


class AboutUsView(LoginRequiredMixin, TemplateView):
    template_name = 'about-us.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'account_login'

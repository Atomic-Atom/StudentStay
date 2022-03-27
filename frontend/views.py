from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView

from properties.models import Property, PropertyImage


# Create your views here.

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'account_login'

    def get_context_data(self, **kwargs):
        campus = self.request.GET.get('campus', None)
        if campus:
            properties = Property.objects.filter(is_active=True, campus=campus)
        else:
            properties = Property.objects.filter(is_active=True)
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'properties': properties,
            'campus': campus
        })
        return context


class PropertyView(LoginRequiredMixin, TemplateView):
    template_name = 'property.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'account_login'

    def get_context_data(self, **kwargs):
        context = super(PropertyView, self).get_context_data(**kwargs)
        pk = kwargs.get('pk')
        context.update({
            'property': Property.objects.get(pk=pk),
            'images': PropertyImage.objects.filter(property__pk=pk)
        })
        return context

    def get(self, request, *args, **kwargs):
        """ On get request check if primary key exists in database"""
        try:
            Property.objects.get(pk=kwargs.get('pk', None))
        except Property.DoesNotExist:
            return HttpResponseRedirect(reverse('home-page'))
        return super(PropertyView, self).get(request, *args, **kwargs)

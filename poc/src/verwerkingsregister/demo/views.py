import logging

from django.conf import settings
from django.contrib import messages
from django.urls import reverse
from django.views.generic import ListView, UpdateView
from django.utils.translation import ugettext_lazy as _

from .tests.factories import VergunningsAanvraagFactory
from .models import VergunningsAanvraag, ZaakStatus
from .kadesterservice import client as kadaster_client


logger = logging.getLogger(__name__)


class VergunningsAanvraagList(ListView):
    model = VergunningsAanvraag

    def dispatch(self, request, *args, **kwargs):
        # Ofcourse, this is for demo purposes.
        count = self.get_queryset().count()
        if count == 0:
            VergunningsAanvraagFactory.create()

        return super().dispatch(request, *args, **kwargs)


class VergunningsAanvraagPreview(UpdateView):
    model = VergunningsAanvraag
    template_name_suffix = '_preview'
    fields = []

    def form_valid(self, form):
        self.object.zaakstatus = ZaakStatus.in_behandeling
        self.object.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'ZaakStatus': ZaakStatus,
        })
        return context

    def get_success_url(self):
        return reverse('demo:update', kwargs={'pk': self.object.pk})


class VergunningsAanvraagUpdate(UpdateView):
    model = VergunningsAanvraag
    template_name_suffix = '_update'
    fields = ['zaakstatus', ]

    def form_valid(self, form):
        messages.add_message(self.request, messages.INFO, _('Aanvraag is {}.'.format(form.instance.get_zaakstatus_display())))

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        try:
            # Retrieve Kadaster data.
            kadaster_data = kadaster_client.get(
                self.object.lokatie_postcode,
                '{}{}'.format(self.object.lokatie_huisnummer_toevoeging, self.object.lokatie_huisnummer),
                city_name=self.object.lokatie_plaats,
                # This is the most important part: Specify which process step is performed here. The ID is taken from the
                # Verwerkingsregister.
                process_id=1,
            )
        except Exception as e:
            logger.exception(e)
            kadaster_data = {}

        context = super().get_context_data(**kwargs)
        context.update({
            'kadaster_data': kadaster_data,
            'kadaster_href': kadaster_data['_links']['self']['href'] if kadaster_data else '',
            'GOOGLE_API_KEY': settings.GOOGLE_API_KEY,
            'ZaakStatus': ZaakStatus,
        })

        return context

    def get_success_url(self):
        return reverse('demo:list')

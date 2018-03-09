from django.conf import settings
from django.utils.translation import ugettext_lazy as _
import urllib.parse

import requests


class Client(object):
    def get(self, postal_code, number, city_name=None, process_id=None):
        """
        Haha, as if the Kadaster API supports postal code requests... but let's assume it does since several
        alternatives that are not official support this just fine.

        :param postal_code: The postal code.
        :param number: The house number.
        :param city_name: Name of the city. Normally not needed but needed to get some demo data.
        :param process_id: The process ID for the Verwerkingsregister.

        :return:
        """
        resource_url = '/api/v1/perceel'
        params = {
            'kadastraleGemeentenaam': city_name,
        }

        url = '{}{}?{}'.format(settings.KADASTER_SERVICE_URL, resource_url, urllib.parse.urlencode(params))

        # Headers for the NLX layer for logging the required Verwerkingsregister properties.
        headers = {
            'X-NLX-Request-Process-Id': str(process_id),
            # Could be taken from settings.
            'X-NLX-Request-Application-Id': 'DEMO-APP',
            'X-NLX-Request-User-Id': 'DEMO-MDW',
            # Typically specified as ?fields= but Kadaster does not support this (although its in the DSO guidelines).
            'X-NLX-Request-Data-Elements': ', '.join([
                'KadastraalObjectIdentificatie',
                'Perceelgrootte',
                'Burgerservicenummer',
            ]),
            # Typically required for the private Kadaster service request, but not actually used here.
            'X-NLX-Subject-Identifier': 'Burgerservicenummer=342641736'
        }

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(_('Ongeldig antwoord van service.'))

        data = response.json()['_embedded']

        if 'results' not in data or len(data['results']) == 0:
            raise Exception(_('Geen kadastrale objecten gevonden.'))

        return data['results'][0]


client = Client()
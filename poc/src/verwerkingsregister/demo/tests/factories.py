import factory
import factory.fuzzy

from ..models import ZaakType


class PersoonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'demo.Persoon'

    achternaam = factory.fuzzy.FuzzyChoice(choices=['Bekker', 'Boer', 'Hotting', 'Jeukendrup', 'Riemer'])
    voornaam = factory.fuzzy.FuzzyChoice(choices=['Joeri', 'Johan', 'Eelco', 'Bart', 'Geert-Johan'])
    adres = factory.fuzzy.FuzzyText(length=50)


locations = dict([
    ('Haarlem ', '2011 RD'),  # LOL, a space is needed for Haarlem.
    ('Amsterdam', '1015 CJ'),
    ('Utrecht', '3512 GG'),
    ('Zaanstad', '1506 MZ'),
    ('Nijmegen', '6511 PS'),
    ('Hoorn', '1625 HV'),
    ('Tilburg', '5038 TC'),
    ('Eindhoven', '5611 EM'),
])


class VergunningsAanvraagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'demo.VergunningsAanvraag'

    aanvrager = factory.SubFactory(PersoonFactory)
    zaaktype = ZaakType.bouwvergunningsaanvraag

    lokatie_plaats = factory.fuzzy.FuzzyChoice(choices=locations.keys())
    lokatie_postcode = factory.LazyAttribute(lambda o: locations[o.lokatie_plaats])
    lokatie_huisnummer = factory.fuzzy.FuzzyInteger(1, 50)

    onderwerp = factory.fuzzy.FuzzyChoice(choices=['Dakkapel', 'Tuinhuis', 'Carport', 'Extra verdieping'])
    toelichting = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris sagittis dui nec venenatis ' \
                  'porttitor. Nam posuere imperdiet velit ut dignissim. Proin scelerisque dignissim tellus a ornare. ' \
                  'Praesent rutrum viverra molestie. Aenean accumsan hendrerit convallis. Aliquam erat volutpat. Nam ' \
                  'facilisis egestas lectus, nec tincidunt libero euismod ac. Aliquam et est purus. Suspendisse vel ' \
                  'posuere nisl. In in rhoncus massa, eu tristique enim. Aliquam id luctus libero.'


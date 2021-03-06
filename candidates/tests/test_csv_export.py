from django.test import TestCase

from ..models import PopItPerson
from ..csv_helpers import list_to_csv
from fake_popit import get_example_popit_json


class CSVTests(TestCase):
    def setUp(self):
        # The second person's name (and party name) have diacritics in
        # them to test handling of Unicode when outputting to CSV.
        self.people = [
            PopItPerson.create_from_dict(
                get_example_popit_json(person_json_filename)['result']
            )
            for person_json_filename in
            (
                'persons_2009_embed=membership.organization.json',
                'persons-1953_embed=membership.organization.json',
            )
        ]

    def test_as_dict(self):
        person_dict = self.people[0].as_dict
        self.assertEqual(len(person_dict), 18)
        self.assertEqual(person_dict['id'], "2959")

    def test_csv_output(self):
        example_output = '' + \
          'name,id,party,constituency,mapit_id,mapit_url,gss_code,twitter_username,facebook_page_url,party_ppc_page_url,gender,facebook_personal_url,email,homepage_url,wikipedia_url,birth_date,parlparse_id,theyworkforyou_url\r\n' + \
          'Tessa Jowell,2959,Labour Party,Dulwich and West Norwood,65808,http://mapit.mysociety.org/area/65808,E14000673,,,,,,jowell@example.com,,,,uk.org.publicwhip/person/10326,http://www.theyworkforyou.com/mp/10326\r\n' + \
          'Daith\xc3\xad McKay,1953,Sinn F\xc3\xa9in,North Antrim,66135,http://mapit.mysociety.org/area/66135,N06000012,,,,male,,,,,,,\r\n'
        self.assertEqual(
            list_to_csv([p.as_dict for p in self.people]),
            example_output,
        )

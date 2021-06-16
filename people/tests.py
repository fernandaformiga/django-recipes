from unittest import TestCase, mock
from .models import Person

class TestPersonMock(TestCase):
    # test with mock

    def test_person_mock(self):
        mock_person = mock.Mock(spec=Person)
        self.assertIsInstance(mock_person, Person)
         
class TestPerson(TestCase):
    # set up person for testing

    def setUp(self):
        Person.objects.create(name="José",
                              age="35",
                              occupation="restaurant owner")
        
    def test_person_is_created(self):
        person = Person.objects.get(name="José")
        self.assertEqual(person.occupation, "restaurant owner")
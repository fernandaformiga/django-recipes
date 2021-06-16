from unittest import TestCase, mock
from .models import Recipe

class TestRecipeMock(TestCase):
    # test with mock

    def test_recipe_mock(self):
        mock_recipe = mock.Mock(spec=Recipe)
        self.assertIsInstance(mock_recipe, Recipe)
         
class TestRecipe(TestCase):
    # set up recipe for testing

    def setUp(self):
        Recipe.objects.create(person=None,
                              recipe_name="sushi",
                              ingredients="salmão, nori, gohan",
                              prep="xxxxxxxxxx",
                              prep_time=60,
                              category="comida japonesa")
        
    def test_recipe_is_created(self):
        sushi = Recipe.objects.get(recipe_name="sushi")
        self.assertEqual(sushi.prep_time, 60)
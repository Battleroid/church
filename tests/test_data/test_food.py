# -*- coding: utf-8 -*-

from church.utils import pull

from . import DummyCase


class FoodTestCase(DummyCase):
    def test_vegetable(self):
        result = self.church.food.vegetable()
        parent_file = pull('vegetables', self.church.food.lang)
        self.assertIn(result + '\n', parent_file)

    def test_fruit(self):
        result = self.church.food.fruit_or_berry()
        parent_file = pull('fruits_berries', self.church.food.lang)
        self.assertIn(result + '\n', parent_file)

    def test_dish(self):
        result = self.church.food.dish()
        parent_file = pull('dishes', self.church.food.lang)
        self.assertIn(result + '\n', parent_file)

    def test_drink(self):
        result = self.church.food.drink()
        parent_file = pull('drinks', self.church.food.lang)
        self.assertIn(result + '\n', parent_file)

    def test_spices(self):
        result = self.church.food.spices()
        parent_file = pull('spices', self.church.food.lang)
        self.assertIn(result + '\n', parent_file)

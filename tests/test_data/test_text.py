# -*- coding: utf-8 -*-

from church import _common as common
from church.utils import pull

from . import DummyCase


class TextTestCase(DummyCase):
    def test_sentence(self):
        result = self.church.text.sentence() + '\n'
        parent_file = pull('text', self.church.text.lang)
        self.assertIn(result, parent_file)

    def test_title(self):
        result = self.church.text.title() + '\n'
        parent_file = pull('text', self.church.text.lang)
        self.assertIn(result, parent_file)

    def test_lorem_ipsum(self):
        result = self.church.text.lorem_ipsum(quantity=2)
        self.assertIsNot(result, None)
        self.assertIsInstance(result, str)

    def test_words(self):
        result = self.church.text.words()
        self.assertEqual(len(result), 5)

        result = self.church.text.words(quantity=1)
        self.assertEqual(len(result), 1)

    def test_word(self):
        result = self.church.text.word()
        parent_file = pull('words', self.church.text.lang)
        self.assertIn(result + '\n', parent_file)

    def test_swear_word(self):
        result = self.church.text.swear_word()
        parent_file = pull('swear_words', self.church.text.lang)
        self.assertIn(result + '\n', parent_file)

    def test_naughty_strings(self):
        result = self.church.text.naughty_strings()
        self.assertTrue(len(result) > 10)
        self.assertIsInstance(result, list)

    def test_quote_from_movie(self):
        result = self.church.text.quote()
        parent_file = pull('quotes', self.church.text.lang)
        self.assertIn(result + '\n', parent_file)

    def test_color(self):
        result = self.church.text.color()
        parent_file = pull('colors', self.church.text.lang)
        self.assertIn(result + '\n', parent_file)

    def test_hex_color(self):
        result = self.church.text.hex_color()
        self.assertIn('#', result)

    def test_emoji(self):
        result = self.church.text.emoji()
        self.assertIn(result, common.EMOJI)

    def test_hashtags(self):
        result = self.church.text.hashtags(quantity=5)
        self.assertEqual(len(result), 5)

        result = self.church.text.hashtags(quantity=1, category='general')
        self.assertIn(result[0], common.HASHTAGS['general'])

    def test_weather(self):
        result = self.church.text.weather(scale='c').split(' ')
        temp, scale = float(result[0]), result[1]
        self.assertEqual(scale, '°C')
        self.assertTrue((temp >= -30) and (temp <= 40))

        result = self.church.text.weather(scale='f', a=0, b=10).split(' ')
        temp, scale = float(result[0]), result[1]
        self.assertEqual(scale, '°F')
        self.assertTrue((temp >= 0) and (temp <= (10 * 1.8) + 32))

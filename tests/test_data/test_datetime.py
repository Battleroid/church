# -*- coding: utf-8 -*-

from church.utils import pull

from . import DummyCase


class DatetimeTestCase(DummyCase):
    def test_day_of_week(self):
        result = self.church.datetime.day_of_week() + '\n'
        self.assertGreater(len(result), 4)

        result_abbr = self.church.datetime.day_of_week(abbr=True)
        self.assertTrue(len(result_abbr) < 6 or '.' in result_abbr)

    def test_month(self):
        result = self.church.datetime.month() + '\n'
        self.assertGreater(len(result), 3)

        result_abbr = self.church.datetime.month(abbr=True)
        self.assertIsInstance(result_abbr, str)

    def test_year(self):
        result = self.church.datetime.year(from_=2000, to_=2016)
        self.assertTrue((result >= 2000) and (result <= 2016))

    def test_periodicity(self):
        result = self.church.datetime.periodicity()
        parent_file = pull('periodicity', self.church.datetime.lang)
        self.assertIn(result + '\n', parent_file)

    def test_day_of_month(self):
        result = self.church.datetime.day_of_month()
        self.assertTrue((result >= 1) or (result <= 31))

    def test_birthday(self):
        result = self.church.datetime.birthday()
        self.assertIsInstance(result, str)

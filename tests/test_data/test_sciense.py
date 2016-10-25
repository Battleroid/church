# -*- coding: utf-8 -*-

import church._common as common
from church.utils import pull

from . import DummyCase


class ScienceTestCase(DummyCase):
    def test_math_formula(self):
        result = self.church.science.math_formula()
        self.assertIn(result, common.MATH_FORMULAS)

    def test_article_on_wiki(self):
        result = self.church.science.article_on_wiki()
        parent_file = pull('science_wiki', self.church.science.lang)
        self.assertIn(result + '\n', parent_file)

    def test_scientist(self):
        result = self.church.science.scientist()
        parent_file = pull('scientist', self.church.science.lang)
        self.assertIn(result + '\n', parent_file)

    def test_chemical_element(self):
        result = self.church.science.chemical_element(name_only=True)
        self.assertGreater(len(result), 2)

        _result = self.church.science.chemical_element(name_only=False)
        self.assertIsInstance(_result, dict)

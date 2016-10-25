# -*- coding: utf-8 -*-

import church._common as common
from church.utils import pull

from . import DummyCase


class BusinessTestCase(DummyCase):
    def test_company_type(self):
        result = self.church.business.company_type()
        self.assertTrue(len(result) > 8)

    def test_company(self):
        result = self.church.business.company()
        parent_file = pull('company', self.church.business.lang)
        self.assertIn(result + '\n', parent_file)

    def test_copyright(self):
        result = self.church.business.copyright()
        copyright_symbol = '©'
        self.assertIn(copyright_symbol, result)
        self.assertTrue(len(result) > 4)

    def test_currency_sio(self):
        result = self.church.business.currency_iso()
        self.assertIn(result, common.CURRENCY)

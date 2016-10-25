# -*- coding: utf-8 -*-

import re

import church._common as common
from church.utils import pull

from . import DummyCase


class PersonalTestCase(DummyCase):
    def test_age(self):
        result = self.church.personal.age(mx=55)
        self.assertTrue(result <= 55)

    def test_name(self):
        result = self.church.personal.name()
        parent_file = pull('f_names', self.church.personal.lang)
        self.assertIn(result + '\n', parent_file)

        result = self.church.personal.name('m')
        parent_file = pull('m_names', self.church.personal.lang)
        self.assertIn(result + '\n', parent_file)

    def test_telephone(self):
        result = self.church.personal.telephone()
        self.assertTrue(len(result) >= 11)

        mask = '+5 (###)-###-##-##'
        result2 = self.church.personal.telephone(mask=mask)
        head = result2.split(' ')[0]
        self.assertEqual(head, '+5')

    def test_surname(self):
        if self.church.personal.lang == 'ru':
            result = self.church.personal.surname('f')
            parent_file = pull('f_surnames', self.church.personal.lang)
            self.assertIn(result + '\n', parent_file)

            result = self.church.personal.surname('m')
            parent_file = pull('m_surnames', self.church.personal.lang)
            self.assertIn(result + '\n', parent_file)
        else:
            result = self.church.personal.surname()
            parent_file = pull('surnames', self.church.personal.lang)
            self.assertIn(result + '\n', parent_file)

    def test_full_name(self):
        result = self.church.personal.full_name('f')
        _result = result.split(' ')
        self.assertIsInstance(_result, list)

    def test_username(self):
        result = self.church.personal.username()
        self.assertTrue(re.match(r'^[a-zA-Z0-9_.-]+$', result))

        result = self.church.personal.username('f')
        self.assertTrue(re.match(r'^[a-zA-Z0-9_.-]+$', result))

    def test_twitter(self):
        result = self.church.personal.twitter('f')
        self.assertIsNotNone(result)

        _result = self.church.personal.twitter('m')
        self.assertIsNotNone(_result)

    def test_facebook(self):
        result = self.church.personal.facebook('f')
        self.assertIsNotNone(result)

        _result = self.church.personal.facebook('m')
        self.assertIsNotNone(_result)

    def test_wmid(self):
        result = self.church.personal.wmid()
        self.assertEqual(len(result), 12)

    def test_paypal(self):
        result = self.church.personal.paypal()
        self.assertIsNotNone(result)

    def test_yandex_money(self):
        result = self.church.personal.yandex_money()
        self.assertEqual(len(result), 14)

    def test_password(self):
        plain = self.church.personal.password(length=15)
        self.assertEqual(len(plain), 15)

        md5 = self.church.personal.password(algorithm='md5')
        self.assertEqual(len(md5), 32)

        sha1 = self.church.personal.password(algorithm='sha1')
        self.assertEqual(len(sha1), 40)

        sha256 = self.church.personal.password(algorithm='sha256')
        self.assertEqual(len(sha256), 64)

        sha512 = self.church.personal.password(algorithm='sha512')
        self.assertEqual(len(sha512), 128)

    def test_email(self):
        result = self.church.personal.email()
        self.assertTrue(
            re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
                     result))

    def test_home_page(self):
        result = self.church.personal.home_page()
        self.assertTrue(re.match(r'http[s]?://(?:[a-zA-Z]|[0-9]|'
                                 r'[$-_@.&+]|[!*\(\),]|'
                                 r'(?:%[0-9a-fA-F][0-9a-fA-F]))+', result))

    def test_subreddit(self):
        result = self.church.personal.subreddit()
        self.assertIn(result, common.SUBREDDITS)

        full_result = self.church.personal.subreddit(full_url=True)
        self.assertTrue(len(full_result) > 20)

        result_nsfw = self.church.personal.subreddit(nsfw=True)
        self.assertIn(result_nsfw, common.SUBREDDITS_NSFW)

        full_result = self.church.personal.subreddit(nsfw=True, full_url=True)
        self.assertTrue(len(full_result) > 20)

    def test_bitcoin(self):
        result = self.church.personal.bitcoin()
        self.assertEqual(len(result), 34)

    def test_cvv(self):
        result = self.church.personal.cvv()
        self.assertTrue((100 <= result) and (result <= 999))

    def test_credit_card_number(self):
        result = self.church.personal.credit_card_number()
        self.assertTrue(re.match(r'[\d]+((-|\s)?[\d]+)+', result))

    def test_expiration_date(self):
        result = self.church.personal.credit_card_expiration_date(mi=16, mx=25)
        year = result.split('/')[1]
        self.assertTrue((int(year) >= 16) and (int(year) <= 25))

    def test_cid(self):
        result = self.church.personal.cid()
        self.assertTrue((1000 <= result) and (result <= 9999))

    def test_gender(self):
        result = self.church.personal.gender() + '\n'
        self.assertIn(result, pull('gender', self.church.personal.lang))

        symbol = self.church.personal.gender(symbol=True)
        self.assertIn(symbol, common.GENDER_SYMBOLS)

    def test_height(self):
        result = self.church.personal.height(from_=1.60, to_=1.90)
        self.assertTrue(result.startswith('1'))
        self.assertIsInstance(result, str)

    def test_weight(self):
        result = self.church.personal.weight(from_=40, to_=60)
        self.assertTrue((result >= 40) and (result <= 60))

    def test_blood_type(self):
        result = self.church.personal.blood_type()
        self.assertIn(result, common.BLOOD_GROUPS)

    def test_sexual_orientation(self):
        result = self.church.personal.sexual_orientation()
        parent_file = pull('sexuality', self.church.personal.lang)
        self.assertIn(result + '\n', parent_file)

        symbol = self.church.personal.sexual_orientation(symbol=True)
        self.assertIn(symbol, common.SEXUALITY_SYMBOLS)

    def test_profession(self):
        result = self.church.personal.profession()
        parent_file = pull('professions', self.church.personal.lang)
        self.assertIn(result + '\n', parent_file)

    def test_university(self):
        result = self.church.personal.university()
        parent_file = pull('university', self.church.personal.lang)
        self.assertIn(result + '\n', parent_file)

    def test_qualification(self):
        result = self.church.personal.qualification()
        parent_file = pull('qualifications', self.church.personal.lang)
        self.assertIn(result + '\n', parent_file)

    def test_language(self):
        result = self.church.personal.language()
        parent_file = pull('languages', self.church.personal.lang)
        self.assertIn(result + '\n', parent_file)

    def test_favorite_movie(self):
        result = self.church.personal.favorite_movie()
        parent_file = pull('movies', self.church.personal.lang)
        self.assertIn(result + '\n', parent_file)

    def test_favorite_music_genre(self):
        result = self.church.personal.favorite_music_genre()
        self.assertIn(result, common.FAVORITE_MUSIC_GENRE)

    def test_worldview(self):
        result = self.church.personal.worldview()
        parent_file = pull('worldview', self.church.personal.lang)
        self.assertIn(result + '\n', parent_file)

    def test_views_on(self):
        result = self.church.personal.views_on()
        parent_file = pull('views_on', self.church.personal.lang)
        self.assertIn(result + '\n', parent_file)

    def test_political_views(self):
        result = self.church.personal.political_views()
        parent_file = pull('political_views', self.church.personal.lang)
        self.assertIn(result + '\n', parent_file)

    def test_avatar(self):
        result = self.church.personal.avatar()
        self.assertTrue(len(result) > 20)

    def test_vehicle(self):
        result = self.church.personal.vehicle()
        self.assertIn(result, common.THE_VEHICLES)

# coding: utf-8

"""
    localhost:8088

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 5.1.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import wazo_appgateway_client
from wazo_appgateway_client.api.sounds_api import SoundsApi  # noqa: E501
from wazo_appgateway_client.rest import ApiException


class TestSoundsApi(unittest.TestCase):
    """SoundsApi unit test stubs"""

    def setUp(self):
        self.api = wazo_appgateway_client.api.sounds_api.SoundsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sounds_get(self):
        """Test case for sounds_get

        List all sounds.  # noqa: E501
        """
        pass

    def test_sounds_sound_id_get(self):
        """Test case for sounds_sound_id_get

        Get a sound's details.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
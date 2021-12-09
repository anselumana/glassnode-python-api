import unittest
from glassnode import GlassnodeClient, GlassnodeClientException
from tests.utils import get_api_key

api_key = get_api_key()

class TestGlassnodeClient(unittest.TestCase):
    def test_instanciation(self):
        GlassnodeClient(api_key)
        self.assertEqual(1, 1)
    
    def test_get_addresses_count(self):
        client = GlassnodeClient(api_key)
        client.get("addresses", "count", {"a": "BTC", "s": "1638403200"})
        self.assertEqual(1, 1)
    
    def test_bad_request_raises_exception(self):
        client = GlassnodeClient(api_key)
        e = None
        try:
            client.get("addresses", "count", {"a": "non existing asset"})
        except Exception as ex:
            e = ex
        self.assertIsInstance(e, GlassnodeClientException)

    
    def test_unauthorized_request_raises_exception(self):
        client = GlassnodeClient("invalid API key")
        e = None
        try:
            client.get("addresses", "count")
        except Exception as ex:
            e = ex
        self.assertIsInstance(e, GlassnodeClientException)
    
    def test_not_found_request_raises_exception(self):
        client = GlassnodeClient(api_key)
        e = None
        try:
            client.get("this endpoint", "does not exist")
        except Exception as ex:
            e = ex
        self.assertIsInstance(e, GlassnodeClientException)
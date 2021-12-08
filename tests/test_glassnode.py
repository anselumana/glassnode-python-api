import unittest
from glassnode import GlassnodeClient

class TestGlassnode(unittest.TestCase):
    def test_instanciation(self):
        client = GlassnodeClient()
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()
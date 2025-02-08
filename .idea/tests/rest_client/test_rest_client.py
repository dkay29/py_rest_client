import unittest
from rest_client import RestClient

class TestRestClient(unittest.TestCase):
    def setUp(self):
        self.client = RestClient("https://localhost:9000/api/")

    def test_get_posts(self):
        response = self.client.get("posts")
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

if __name__ == "__main__":
    unittest.main()

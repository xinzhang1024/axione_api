
import unittest

from fastapi.testclient import TestClient

from main import app


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_post_200(self):
        mock_request = {
          "department": "95",
          "surface": 60,
          "max_rent": 2000
        }

        response = self.client.post('/search', json=mock_request)
        self.assertEqual(response.status_code, 200)

import unittest
from unittest.mock import MagicMock
from inventory_client import Client
from get_book_titles import get_book_title


class MockAPIClassInterface:
    def __init__(self):
        self.expect = ["17645_a1", "17645_a2"]

    def mock(self):
        client_mock = Client()
        client_mock.getBook = MagicMock(return_value=self.expect)
        return client_mock.getBook()


class TestInventoryService(unittest.TestCase):
    def setUp(self):
        self.mockAPI = MockAPIClassInterface()
        self.client = Client()
        self.expect = ["17645_a1", "17645_a2"]

    def test_mock_client(self):
        self.assertEqual(self.mockAPI.mock(), self.expect)

    def test_live_server(self):
        self.assertEqual(get_book_title(self.client, ["1", "2"]), self.expect)


if __name__ == "__main__":
    unittest.main()

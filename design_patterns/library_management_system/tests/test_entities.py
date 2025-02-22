import unittest

from libs.entities import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(1, "Roberto")

    def test_get_id(self):
        self.assertEquals(self.user.get_id(), self.user.id)

    def tearDown(self):
        del self.user


if __name__ == "__main__":
    unittest.main()
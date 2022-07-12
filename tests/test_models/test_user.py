#!/usr/bin/python3
"""
Unittest for User
"""

import unittest
from models.user import User
from datetime import datetime
from time import sleep


class testUser(unittest.TestCase):
    """
    Test for User
    """
    def test_str_email(self):
        """
        Check if email is a string
        """
        self.assertEqual(str, type(User.email))

    def test_str_password(self):
        """
        Check if password is a string
        """
        self.assertEqual(str, type(User.password))

    def test_str_first_name(self):
        """
        Check if first_name is a string
        """
        self.assertEqual(str, type(User.first_name))

    def test_str_last_name(self):
        """
        Check if last_name is a string
        """
        self.assertEqual(str, type(User.last_name))

    def test_unique_id(self):
        """
        Check if the User id in unique
        """
        instance1 = User()
        instance2 = User()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_instance_createdat(self):
        """
        Check if created_at is a intance of User
        """
        self.assertTrue(hasattr(User(), "created_at"), True)

    def test_instance(self):
        """
        Check if updated_at is a intance of User
        """
        self.assertTrue(hasattr(User(), "updated_at"), True)

    def test_public_datetime(self):
        """
        Test for a make public datetime
        """
        self.assertEqual(datetime, type(User().created_at))

    def test_public_datetime_updated(self):
        """
        Test for a make public datetime
        """
        self.assertEqual(datetime, type(User().updated_at))

    def test_less_time_createdat(self):
        """
        Check less time in created_at
        """
        instance1 = User()
        sleep(0.2)
        instance2 = User()
        self.assertLess(instance1.created_at, instance2.created_at)

    def test_less_time_updatedat(self):
        """
        Check less time in updated_at
        """
        instance1 = User()
        sleep(0.2)
        instance2 = User()
        self.assertLess(instance1.updated_at, instance2.updated_at)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""
Unittest for City
"""

import unittest
from models.city import City
from datetime import datetime
from time import sleep


class testCity(unittest.TestCase):
    """
    Test for City
    """
    def test_str_stateid(self):
        """
        Check if state_id is a string
        """
        self.assertEqual(str, type(City.state_id))

    def test_str_password(self):
        """
        Check if name is a string
        """
        self.assertEqual(str, type(City.name))

    def test_unique_id(self):
        """
        Check if the review id in unique
        """
        instance1 = City()
        instance2 = City()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_instance_createdat(self):
        """
        Check if created_at is a intance of City
        """
        self.assertTrue(hasattr(City(), "created_at"), True)

    def test_instance(self):
        """
        Check if updated_at is a intance of City
        """
        self.assertTrue(hasattr(City(), "updated_at"), True)

    def test_public_datetime(self):
        """
        Test for a make public datetime
        """
        self.assertEqual(datetime, type(City().created_at))

    def test_public_datetime_updated(self):
        """
        Test for a make public datetime
        """
        self.assertEqual(datetime, type(City().updated_at))

    def test_less_time_createdat(self):
        """
        Check less time in created_at
        """
        instance1 = City()
        sleep(0.2)
        instance2 = City()
        self.assertLess(instance1.created_at, instance2.created_at)

    def test_less_time_updatedat(self):
        """
        Check less time in updated_at
        """
        instance1 = City()
        sleep(0.2)
        instance2 = City()
        self.assertLess(instance1.updated_at, instance2.updated_at)


if __name__ == '__main__':
    unittest.main()

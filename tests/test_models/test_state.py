#!/usr/bin/python3
"""
Unittest for State
"""

import unittest
from models.state import State
from datetime import datetime
from time import sleep


class testState(unittest.TestCase):
    """
    Test for State
    """
    def test_str_name(self):
        """
        Check if name is a string
        """
        self.assertEqual(str, type(State.name))

    def test_unique_id(self):
        """
        Check if the review id in unique
        """
        instance1 = State()
        instance2 = State()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_instance_createdat(self):
        """
        Check if created_at is a intance of State
        """
        self.assertTrue(hasattr(State(), "created_at"), True)

    def test_instance(self):
        """
        Check if updated_at is a intance of State
        """
        self.assertTrue(hasattr(State(), "updated_at"), True)

    def test_public_datetime(self):
        """
        Test for a make public datetime
        """
        self.assertEqual(datetime, type(State().created_at))

    def test_public_datetime_updated(self):
        """
        Test for a make public datetime
        """
        self.assertEqual(datetime, type(State().updated_at))

    def test_less_time_createdat(self):
        """
        Check less time in created_at
        """
        instance1 = State()
        sleep(0.2)
        instance2 = State()
        self.assertLess(instance1.created_at, instance2.created_at)

    def test_less_time_updatedat(self):
        """
        Check less time in updated_at
        """
        instance1 = State()
        sleep(0.2)
        instance2 = State()
        self.assertLess(instance1.updated_at, instance2.updated_at)


if __name__ == '__main__':
    unittest.main()

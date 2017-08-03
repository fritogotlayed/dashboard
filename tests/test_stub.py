"""
The MIT License (MIT)
Copyright (c) 2017 AOUtils-Team

For full license details please see the LICENSE file located in the root folder
of the project.
"""
import unittest


class TestStub(unittest.TestCase):
    """Class for project stub to run a unit test"""

    def setUp(self):
        """Test init code

        This is typically where you would set up items that are used in each
        test in this class. I'm just setting an item under test for now as a
        demo.
        """
        self._value = True

    def tearDown(self):
        """Test cleanup code

        This is where we typically clean up after any tests. Things like
        removing a temp folder or file would be done here. This test doesn't
        really do any of that. As a demo I'm setting our test value to none.
        """
        self._value = None

    def test_stub(self):
        """Test that our class can hold data

        Verify that our class level variable _value is defaulted with a value
        of True as part of the test initialization.
        """
        self.assertEqual(self._value, True)

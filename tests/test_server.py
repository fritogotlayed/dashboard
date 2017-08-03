"""
The MIT License (MIT)
Copyright (c) 2017 AOUtils-Team

For full license details please see the LICENSE file located in the root folder
of the project.
"""
import unittest
import dashboard.server as server

from tests import capture_output


class TestServer(unittest.TestCase):
    """Tests for the server module"""

    @staticmethod
    def test_main():
        """Test main entry point of server module"""
        # Act
        with capture_output() as (out, err):
            server.main()

            # Assert
            output = out.getvalue().strip()
            error = err.getvalue().strip()
            assert output == 'main stub'
            assert error == ''

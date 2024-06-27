#!/usr/bin/python3
"""Test for console.py"""

import unittest

from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test the console"""

    def test_prompt(self):
        """Test the prompt"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_do_create(self):
        """Test the do_create method"""
        pass

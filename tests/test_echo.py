#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess


class TestEcho(unittest.TestCase):

    def setUp(self):
        self.parser = echo.create_parser()

    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()
        self.assertEquals(stdout, usage)

    def test_upper_short(self):
        """ Running with -u returns upper cased text """
        arg_list = ['-u', 'hello']
        namespace = self.parser.parse_args(arg_list)
        self.assertTrue(namespace.upper)

        # Did the program transform our text to uppercase?
        self.assertEqual(echo.main(arg_list), "HELLO")

    def test_upper_long(self):
        """ Running with --upper returns upper cased text """
        arg_list = ['--upper', 'hello']
        namespace = self.parser.parse_args(arg_list)
        self.assertTrue(namespace.upper)

        # Did the program transform our text to uppercase?
        self.assertEqual(echo.main(arg_list), "HELLO")

    def test_lower_short(self):
        """ Running with -l returns lower cased text """
        arg_list = ['--lower', 'HELLO']
        namespace = self.parser.parse_args(arg_list)
        self.assertTrue(namespace.lower)

        # Did the program transform our text to lowercase?
        self.assertEqual(echo.main(arg_list), 'hello')

    def test_lower_long(self):
        """ Running with --lower returns lower cased text """
        arg_list = ['-l', 'HELLO']
        namespace = self.parser.parse_args(arg_list)
        self.assertTrue(namespace.lower)

        # Did the program transform our text to lowercase?
        self.assertEqual(echo.main(arg_list), 'hello')

    def test_title_short(self):
        """ Running with -t returns title cased text """
        arg_list = ['-t', 'title']
        namespace = self.parser.parse_args(arg_list)
        self.assertTrue(namespace.title)

        # Did the program transform text to TitleCase?
        self.assertEqual(echo.main(arg_list), 'Title')

    def test_title_long(self):
        """ Running with --title returns title cased text """
        arg_list = ['--title', 'title']
        namespace = self.parser.parse_args(arg_list)
        self.assertTrue(namespace.title)

        # Did the program transform text to TitleCase?
        self.assertEqual(echo.main(arg_list), 'Title')

    def test_all_options(self):
        """ Running with -ult returns title cased text """
        arg_list = ['-ult', "hello"]
        namespace = self.parser.parse_args(arg_list)
        self.assertTrue(namespace.title and namespace.upper
                        and namespace.lower)

        # Should title case all text
        self.assertEqual(echo.main(arg_list), 'Hello')

    def test_no_options(self):
        """ Running with no options returns unchanged text """
        arg_list = ['Hello']
        namespace = self.parser.parse_args(arg_list)
        self.assertTrue(namespace.title != True and namespace.upper != True
                        and namespace.title != True)

        # Should return input text, not manipulated
        self.assertEqual(echo.main(arg_list), 'Hello')


if __name__ == '__main__':
    unittest.main()

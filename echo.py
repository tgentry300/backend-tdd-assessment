#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "tgentry300"


import sys
import argparse


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
        description='Perform transformation on input text.')
    parser.add_argument(
        '-u', '--upper', action='store_true', help='convert text to uppercase')
    parser.add_argument(
        '-l', '--lower', action='store_true', help='convert text to lowercase')
    parser.add_argument(
        '-t', '--title', action='store_true', help='convert text to titlecase')
    parser.add_argument(
        'text', help='text to be manipulated')

    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    namespace = parser.parse_args(args)
    num_of_true_args = len([n for n in vars(namespace).values() if n is True])
    result = ''

    if namespace.upper:
        result = namespace.text.upper()

    if namespace.lower:
        result = namespace.text.lower()

    if namespace.title:
        result = ''.join(namespace.text.title())

    if num_of_true_args == 0:
        result = namespace.text

    return result


if __name__ == '__main__':
    print(main(sys.argv[1:]))

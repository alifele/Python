#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_boiler_plate
----------------------------------

Tests for `boiler_plate` module.
"""

import unittest

import boiler_plate


class TestBoiler_plate(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        assert(boiler_plate.__version__)

    def tearDown(self):
        pass

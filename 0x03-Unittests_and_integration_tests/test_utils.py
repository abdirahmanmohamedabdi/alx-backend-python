#!/usr/bin/env python3
"""
Test for access_nested_map function
"""
import unittest
import requests
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from typing import Mapping, sequence, Any
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: int) -> None:
        """
        Test access_nested_map function
        """
        response = access_nested_map(nested_map, path)
        self.assertEqual(response, expected)

    @parameterized.expand([
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """
        Test access_nested_map function with exception
        """
        with self.assertRaises(Exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    TestGetJson class
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        """
        Test get_json function
        """
        mock_requests_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_requests_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    TestMemoize class
    """
    def test_memoize(self):
        """
        Test that utils.memoize works
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock_object:
            test = TestClass()
            test.a_property()
            test.a_property()
            mock_object.assert_called_once()

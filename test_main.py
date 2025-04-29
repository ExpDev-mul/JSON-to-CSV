import pytest
from main import flatten_json

def test_flatten_json_with_nested_dict():
    nested_json = {
        "user": {
            "name": "John",
            "details": {
                "age": 30,
                "location": "USA"
            }
        }
    }
    expected_output = {
        "user/name": "John",
        "user/details/age": 30,
        "user/details/location": "USA"
    }
    assert flatten_json(nested_json) == expected_output

def test_flatten_json_with_array():
    nested_json = {
        "user": {
            "name": "John",
            "hobbies": ["reading", "traveling"]
        }
    }
    expected_output = {
        "user/name": "John",
        "user/hobbies": ["reading", "traveling"]
    }
    assert flatten_json(nested_json) == expected_output

def test_flatten_json_with_primitive():
    nested_json = {
        "name": "John",
        "age": 30
    }
    expected_output = {
        "name": "John",
        "age": 30
    }
    assert flatten_json(nested_json) == expected_output

def test_flatten_json_with_empty_dict():
    nested_json = {}
    expected_output = {}
    assert flatten_json(nested_json) == expected_output

def test_flatten_json_with_empty_list():
    nested_json = {
        "items": []
    }
    expected_output = {
        "items": []
    }
    assert flatten_json(nested_json) == expected_output

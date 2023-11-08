import json
import pytest
from unittest.mock import patch
from src.models import OpeningHour
from src.cache.redis import get_opening_hours_from_cache
from src.cache.redis import cache_opening_hours
from src.cache.redis import get_cache_key_from


@pytest.fixture
def mock_redis(monkeypatch):
    mock_redis_conn = patch('src.cache.redis.redis_conn').start()
    yield mock_redis_conn
    patch.stopall()


@pytest.fixture
def opening_hours_data():
    return [
        OpeningHour(type="open", value=36000),
        OpeningHour(type="close", value=64800)
    ]


def test_get_cache_key_from(opening_hours_data):
    cache_key = get_cache_key_from(opening_hours_data)
    expected_value = json.dumps([{"type": "open", "value": 36000}, {"type": "close", "value": 64800}])
    assert cache_key == expected_value


def test_get_opening_hours_from_cache_miss(mock_redis, opening_hours_data):
    mock_redis.get.return_value = None
    result = get_opening_hours_from_cache(opening_hours_data)
    assert result is None
    mock_redis.get.assert_called_once()


def test_cache_opening_hours(mock_redis, opening_hours_data):
    result = "10 AM - 6 PM"
    cache_key = get_cache_key_from(opening_hours_data)
    cache_opening_hours(opening_hours_data, result)
    serialized_data = json.dumps(result)
    mock_redis.setex.assert_called_with(cache_key, 3600, serialized_data)


def test_get_opening_hours_from_cache_hit(mock_redis, opening_hours_data):
    cache_key = get_cache_key_from(opening_hours_data)
    expected_result = "10 AM - 6 PM"
    mock_redis.get.return_value = json.dumps(expected_result)
    result = get_opening_hours_from_cache(opening_hours_data)
    assert result == expected_result
    mock_redis.get.assert_called_with(cache_key)

import redis
import json
from src.settings import REDIS_SERVER
from src.settings import REDIS_PORT
from src.settings import CACHE_TIME

redis_conn = redis.StrictRedis(host=REDIS_SERVER, port=REDIS_PORT)


def get_opening_hours_from_cache(opening_hours):
    cache_key = get_cache_key_from(opening_hours)

    redis_cached_result = redis_conn.get(cache_key)

    if redis_cached_result:
        return json.loads(redis_cached_result)

    return None


def cache_opening_hours(opening_hours, result):
    """Cache the result in Redis with a 1-hour expiration"""

    cache_key = get_cache_key_from(opening_hours)
    redis_conn.setex(cache_key, CACHE_TIME, json.dumps(result))


def get_cache_key_from(opening_hours):
    """Serialize the opening hours list to a JSON string as the cache key"""

    opening_hours_list = [entry.to_dict() for entry in opening_hours]
    return json.dumps(opening_hours_list)

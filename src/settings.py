import os
from src.utils import safe_parse_int


REDIS_SERVER = os.environ.get("REDIS_SERVER", "redis_server")

REDIS_PORT = safe_parse_int(
    os.environ.get("REDIS_PORT"),
    6379
)

CACHE_TIME = safe_parse_int(
    os.environ.get("CACHE_TIME"),
    3600
)

from slowapi import Limiter
from slowapi.util import get_remote_address
from functools import wraps

limiter=Limiter(key_func=get_remote_address, auto_check=True,storage_uri="redis://localhost:6379")

def get_user_id():
    return 1

def custom_limiter():
    def decorator(func):
        @limiter.limit(limit_value='2/minute', key_func=get_remote_address)
        @limiter.limit(limit_value='2/minute', key_func=get_user_id)
        @limiter.limit(limit_value='1/40second', key_func=get_remote_address)
        @limiter.limit(limit_value='1/40second', key_func=get_user_id)
        @wraps(func)
        async def wrapper(*args, **kwargs):
            return await func(*args, **kwargs)
        return wrapper
    return decorator
import json
from redis.asyncio import Redis
from config import REDIS_URL

# Initialize Redis connection
redis = Redis(host='localhost', port=6379, db=0)

async def set_cache(key: str, value: dict, ttl: int):
    """Set cache with a serialized dictionary."""
    # Convert the dictionary to a JSON string
    value_json = json.dumps(value)
    
    # Store the JSON string in Redis with a TTL
    await redis.set(key, value_json, ex=ttl)

async def get_cached_data(key: str):
    """Retrieve and deserialize cached data."""
    value = await redis.get(key)
    if value is not None:
        # Convert JSON string back to dictionary
        return json.loads(value)
    return None  # Return None if key doesn't exist

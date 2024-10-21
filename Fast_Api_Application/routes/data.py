from fastapi import APIRouter, Depends, HTTPException
from auth import get_current_user
from cache import get_cached_data, set_cache

router = APIRouter()

@router.get("/data")
async def get_data(current_user: str = Depends(get_current_user)):
    # Try to get cached data
    cached_data = await get_cached_data("external_data")
    if cached_data:
        return {"data": cached_data}

    # Mock response data since no external API is available
    mock_data = {
        "weather": {
            "temperature": "20°C",
            "condition": "Clear",
            "location": "London"
        },
        "info": "This is mock data since no external API is available."
    }

    # Optionally, simulate a delay to mimic API call
    # import asyncio
    # await asyncio.sleep(1)  # Simulate network delay

    # Store mock data in cache
    await set_cache("external_data", mock_data, ttl=600)
    
    return {"data": mock_data}

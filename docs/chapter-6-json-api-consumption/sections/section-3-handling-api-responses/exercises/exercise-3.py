"""Section 3 Exercise 3 (Bonus/Real-World): Handling Live Weather API Responses.

Implement process_weather_response(response_json) to handle real API data from OpenMeteo.

This exercise uses REAL API data from https://open-meteo.com (public weather API, no auth required).
Develop and test with the sample data below, but ALSO test with a live API call:

    import requests
    response = requests.get(
        'https://api.open-meteo.com/v1/forecast',
        params={'latitude': 37.77, 'longitude': -122.41, 'current': 'temperature_2m,relative_humidity_2m,weather_code,is_day'}
    )
    if response.ok:
        data = response.json()
        # Then pass data to your function

This demonstrates how real API responses may have optional fields, nested structures, and missing data.
"""

# Sample response from OpenMeteo API (San Francisco coordinates: 37.77, -122.41)
SAMPLE_WEATHER_RESPONSE = {
    "latitude": 37.77,
    "longitude": -122.41,
    "generationtime_ms": 1.2,
    "utc_offset_seconds": -25200,
    "timezone": "America/Los_Angeles",
    "timezone_abbreviation": "PDT",
    "elevation": 52.0,
    "current": {
        "time": "2024-04-11T14:30",
        "interval": 900,
        "temperature_2m": 18.5,
        "relative_humidity_2m": 65,
        "weather_code": 80,
        "is_day": 1,
        "wind_speed_10m": 12.3,
    }
}

# Alternate sample with missing/null fields (real API sometimes returns these)
SAMPLE_WEATHER_RESPONSE_INCOMPLETE = {
    "latitude": 51.51,
    "longitude": -0.13,
    "generationtime_ms": 0.8,
    "utc_offset_seconds": 0,
    "timezone": "Europe/London",
    "timezone_abbreviation": "BST",
    "elevation": 12.0,
    "current": {
        "time": "2024-04-11T15:45",
        "interval": 900,
        "temperature_2m": 12.1,
        "relative_humidity_2m": None,  # Missing data
        "weather_code": 61,
        "is_day": 1,
        # wind_speed_10m is missing entirely
    }
}


def process_weather_response(response_json):
    """Process real weather API response and extract/validate key fields.

    Args:
        response_json: Parsed JSON response from OpenMeteo API

    Returns:
        A dictionary with keys:
        - location: String formatted as "latitude,longitude" (e.g., "37.77,-122.41")
        - timezone: Timezone abbreviation (e.g., "PDT") or "Unknown" if missing
        - current_time: Current time string or "N/A" if missing
        - temperature: Temperature in Celsius or None if missing
        - humidity: Relative humidity percentage (0-100) or None if missing
        - weather_code: Integer weather code or None if missing
        - is_day: 1 for daytime, 0 for nighttime, or None if missing
        - has_wind: Boolean indicating if wind_speed_10m is present and valid (non-null)
        - missing_fields: List of expected fields that are null or missing
        - data_quality: String "complete" if all fields present and non-null, "partial" otherwise
    """
    raise NotImplementedError("Implement process_weather_response(response_json)")

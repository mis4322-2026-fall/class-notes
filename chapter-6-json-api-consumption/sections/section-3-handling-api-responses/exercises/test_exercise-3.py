"""Unit tests for Section 3 Exercise 3: Handling Live Weather API Responses."""

import unittest
from exercise_3 import (
    process_weather_response,
    SAMPLE_WEATHER_RESPONSE,
    SAMPLE_WEATHER_RESPONSE_INCOMPLETE,
)


class TestProcessWeatherResponse(unittest.TestCase):
    """Test suite for process_weather_response()."""

    def test_complete_response(self):
        """Test processing a complete, valid weather response."""
        result = process_weather_response(SAMPLE_WEATHER_RESPONSE)

        # Verify structure
        self.assertIsInstance(result, dict)
        required_keys = {
            "location",
            "timezone",
            "current_time",
            "temperature",
            "humidity",
            "weather_code",
            "is_day",
            "has_wind",
            "missing_fields",
            "data_quality",
        }
        self.assertEqual(set(result.keys()), required_keys)

        # Verify values for complete response
        self.assertEqual(result["location"], "37.77,-122.41")
        self.assertEqual(result["timezone"], "PDT")
        self.assertEqual(result["current_time"], "2024-04-11T14:30")
        self.assertAlmostEqual(result["temperature"], 18.5)
        self.assertEqual(result["humidity"], 65)
        self.assertEqual(result["weather_code"], 80)
        self.assertEqual(result["is_day"], 1)
        self.assertTrue(result["has_wind"])
        self.assertEqual(result["missing_fields"], [])
        self.assertEqual(result["data_quality"], "complete")

    def test_incomplete_response(self):
        """Test processing a response with missing/null fields."""
        result = process_weather_response(SAMPLE_WEATHER_RESPONSE_INCOMPLETE)

        # Verify values for incomplete response
        self.assertEqual(result["location"], "51.51,-0.13")
        self.assertEqual(result["timezone"], "BST")
        self.assertIsNone(result["humidity"])  # This field is null
        self.assertFalse(result["has_wind"])  # wind_speed_10m is missing
        self.assertEqual(result["data_quality"], "partial")
        self.assertIn("relative_humidity_2m", result["missing_fields"])

    def test_empty_response(self):
        """Test handling an empty or malformed response."""
        result = process_weather_response({})

        self.assertEqual(result["timezone"], "Unknown")
        self.assertIsNone(result["temperature"])
        self.assertEqual(result["data_quality"], "partial")
        self.assertGreater(len(result["missing_fields"]), 0)

    def test_location_formatting(self):
        """Test that location is formatted correctly as 'lat,lon'."""
        result = process_weather_response(SAMPLE_WEATHER_RESPONSE)
        self.assertRegex(result["location"], r"^-?\d+\.\d+,-?\d+\.\d+$")

    def test_temperature_and_humidity_types(self):
        """Test that temperature and humidity are numeric or None."""
        result = process_weather_response(SAMPLE_WEATHER_RESPONSE)
        self.assertIsInstance(result["temperature"], (int, float, type(None)))
        self.assertIsInstance(result["humidity"], (int, type(None)))
        if result["humidity"] is not None:
            self.assertTrue(0 <= result["humidity"] <= 100)

    def test_is_day_values(self):
        """Test that is_day is 0, 1, or None."""
        result = process_weather_response(SAMPLE_WEATHER_RESPONSE)
        self.assertIn(result["is_day"], [0, 1, None])


if __name__ == "__main__":
    unittest.main()

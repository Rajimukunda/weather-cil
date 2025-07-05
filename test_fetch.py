import unittest
from weather.utils import format_weather

class TestWeatherUtils(unittest.TestCase):
    def test_format_weather(self):
        sample = {
            "name": "Delhi",
            "main": {"temp": 30},
            "weather": [{"description": "clear sky"}]
        }
        result = format_weather(sample)
        self.assertEqual(result, "Weather in Delhi: 30°C, Clear sky")

if __name__ == "__main__":
    unittest.main()

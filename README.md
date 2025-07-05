##Weather Forecast CLI App## 
A simple command-line application to get real-time weather information for any city using the OpenWeatherMap API.

 #Features
1. Get current temperature and weather conditions by city name
2. Displays temperature in Celsius
3. Graceful error handling for invalid inputs or missing API keys
4. Unit tests to ensure utility functionality
5. CI integration using GitHub Actions
# Setup Instructions
Clone the Repository git clone https://github.com/your-username/weather-cli.git cd weather-cli
Create Virtual Environment (Optional but Recommended)
. python -m venv venv

# Install Dependencies
. pip install -r requirements.txt

# Get Your API Key
1. Create a free account at OpenWeatherMap
2. Navigate to API Keys and generate a key 
3. Set it as an environment variable 
#Windows CMD# 
> set OPENWEATHER_API_KEY=your_api_key
# Run the App
python main.py

# Run Tests
python -m unittest discover tests

# Continuous Integration (CI)
.github/workflows/python-ci.yml

# Future Improvements
1. Support hourly/weekly forecast
2. Add support for country codes
3. Output temperatures in Fahrenheit (imperial units)
4. Cache recent requests to reduce API calls
# Project Structure
weather-cli/ ├── main.py ├── requirements.txt ├── README.md ├── weather/ │ ├── init.py │ ├── fetch.py │ └── utils.py ├── tests/ │ ├── init.py │ └── test_fetch.py └── .github/ └── workflows/ └── python-ci.yml

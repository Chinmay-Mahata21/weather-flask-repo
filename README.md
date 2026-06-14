#   Weather App

A simple weather application built with **Flask**, **HTML**, and **CSS** that allows users to search for any city and view its current weather conditions in real time.

## Features

* Search weather by city name
* Display current temperature in Celsius
* Show weather description
* Display weather condition icons
* Responsive and clean user interface
* Secure API key management using `.env`

## Technologies Used

* Python
* Flask
* HTML5
* CSS3
* WeatherAPI
* python-dotenv

## Project Structure

```
weather-app/
│
├── app.py
├── .env
├── .gitignore
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    └── css/
        └── style.css
```

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root and add:

```env
WEATHER_API_KEY=your_api_key_here
```

## Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

## How It Works

1. User enters a city name.
2. Flask receives the request.
3. The application sends a request to WeatherAPI.
4. Weather data is processed and displayed on the webpage.
5. Temperature, weather condition, and icon are shown to the user.

## Future Improvements

* 5-day weather forecast
* Air Quality Index (AQI)
* Wind speed and humidity information
* Geolocation support
* Dark mode
* Search history

## Author

**Chinmay Mahata**

Built as a learning project to practice Flask, API integration, and web development fundamentals.

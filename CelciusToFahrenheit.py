from datetime import datetime, date, time
import streamlit as st
import pandas as pd

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def get_weather_data(lat, lon):
    # You can use any weather API of your choice here to get the weather data.
    # For the sake of this example, I'm simply returning a random temperature.
    return 20.0

def main():
    st.title('Weather Temperature Converter')

    # Get latitude and longitude from user's location
    if st.button('Get My Location'):
        user_location = st.location()
        if user_location:
            lat, lon = user_location['latitude'], user_location['longitude']
            weather_temp_celsius = get_weather_data(lat, lon)
            weather_temp_fahrenheit = celsius_to_fahrenheit(weather_temp_celsius)
            st.write(f"Current Weather Temperature: {weather_temp_celsius:.2f}°C / {weather_temp_fahrenheit:.2f}°F")
        else:
            st.write('Unable to fetch location. Please allow location access.')

    # Input Celsius temperature
    celsius_temp = st.number_input('Enter Celsius temperature:', value=0.0)

    # Convert Celsius to Fahrenheit
    fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)

    # Display the result
    st.write(f'{celsius_temp:.2f}°C is equal to {fahrenheit_temp:.2f}°F')


if __name__ == '__main__':
    main()

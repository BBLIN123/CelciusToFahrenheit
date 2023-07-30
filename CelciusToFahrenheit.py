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

    
    # Input Celsius temperature
    celsius_temp = st.number_input('Enter Celsius temperature:', value=0.0)

    # Convert Celsius to Fahrenheit
    fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)

    # Display the result
    st.write(f'{celsius_temp:.2f}°C is equal to {fahrenheit_temp:.2f}°F')
    
    
    
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "70 °F", "1.2 °F")
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "86%", "4%")
    
    
    
    
    

if __name__ == '__main__':
    main()

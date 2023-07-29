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
    
    data_df = pd.DataFrame(
        {
            "category": [
                "📊 Data Exploration",
                "📈 Data Visualization",
                "🤖 LLM",
                "📊 Data Exploration",
            ],
        }
    )
    
    st.data_editor(
        data_df,
        column_config={
            "category": st.column_config.SelectboxColumn(
                "App Category",
                help="The category of the app",
                width="medium",
                options=[
                    "📊 Data Exploration",
                    "📈 Data Visualization",
                    "🤖 LLM",
                ],
            )
        },
        hide_index=True,
    )
    
    Date_df = pd.DataFrame(
        {
            "appointment": [
                datetime(2024, 2, 5, 12, 30),
                datetime(2023, 11, 10, 18, 0),
                datetime(2024, 3, 11, 20, 10),
                datetime(2023, 9, 12, 3, 0),
            ]
        }
    )
    
    st.data_editor(
        Date_df,
        column_config={
            "appointment": st.column_config.DatetimeColumn(
                "Appointment",
                min_value=datetime(2023, 6, 1),
                max_value=datetime(2025, 1, 1),
                format="D MMM YYYY, h:mm a",
                step=60,
            ),
        },
        hide_index=True,
    )
    
    Progress_df = pd.DataFrame(
        {
            "Progress": [30, 80, 50, 10],
        }
    )
    
    st.data_editor(
        Progress_df,
        column_config={
            "Progress": st.column_config.ProgressColumn(
                "Work in Progress",
                help="The sales volume in USD",
                format="%f'%'",
                min_value=0,
                max_value=100,
            ),
        },
        hide_index=True,
    )
    
    Image_df = pd.DataFrame(
        {
            "apps": [
                "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/5435b8cb-6c6c-490b-9608-799b543655d3/Home_Page.png",
                "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/ef9a7627-13f2-47e5-8f65-3f69bb38a5c2/Home_Page.png",
                "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/31b99099-8eae-4ff8-aa89-042895ed3843/Home_Page.png",
                "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/6a399b09-241e-4ae7-a31f-7640dc1d181e/Home_Page.png",
            ],
        }
    )
    
    st.data_editor(
        Image_df,
        column_config={
            "apps": st.column_config.ImageColumn(
                "Preview Image", help="Streamlit app preview screenshots"
            )
        },
        hide_index=True,
    )

if __name__ == '__main__':
    main()

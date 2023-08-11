from datetime import datetime, date, time
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def get_weather_data(lat, lon):
    # You can use any weather API of your choice here to get the weather data.
    # For the sake of this example, I'm simply returning a random temperature.
    return 20.0

def main():
    st.title('This is not Weather Temperature Converter')


    chart_data = pd.DataFrame(
       np.random.randn(500, 2) / [50, 50] + [-27.634, 152.969],
       columns=['lat', 'lon'])
    manual_data = pd.DataFrame(
        [
            [153.0693972, -27.4402576, 8],
            [152.9693743, -27.634058, 8],
            [153.0141115, -27.4797838, 8],
            [153.0693852, -27.4402576, 8],
            [152.9693823, -27.634058, 8],
            [153.0141005, -27.4797838, 8],
            [153.0694872, -27.4402576, 8],
            [152.9692843, -27.634058, 8],
            [153.0141815, -27.4797838, 8],
            [153.0693772, -27.4402576, 8],
            [152.9693643, -27.634058, 8],
            [153.0141515, -27.4797838, 8],
            [153.0693472, -27.4402576, 8],
            [152.9693343, -27.634058, 8],
            [153.0141215, -27.4797838, 8],
            [153.0693972, -27.4402576, 8],
            [152.9693143, -27.634058, 8],
            [153.0141095, -27.4797838, 8],
            [153.0693882, -27.4402576, 8],
            [152.9693873, -27.634058, 8],
            [153.0141065, -27.4797838, 8],
            [153.0693852, -27.4402576, 8],
            [152.9693833, -27.634058, 8],
            [153.0141045, -27.4797838, 8],
            [153.0683822, -27.4402576, 8],
            [152.9673813, -27.634058, 8],
            [153.0161000, -27.4797838, 8],
            [153.0653879, -27.4402576, 8],
            [152.9643848, -27.634058, 8],
            [153.0131017, -27.4797838, 8],
            [153.0623876, -27.4402576, 8],
            [152.9613845, -27.634058, 8],
            [153.0101014, -27.4797838, 8],
            [153.0693873, -27.4402576, 8],
            [152.9693842, -27.634058, 8],
            [153.093872, -27.4402576, 8],
            [152.9693843, -27.634058, 8],
            [153.0141015, -27.4797838, 8],
            [153.0693872, -27.4402576, 8],
            [152.9693843, -27.634058, 8],
            [153.0141015, -27.4797838, 8],
            [152.9777777, -27.634058, 8],
            [152.9777777, -27.634058, 8],
            [152.9773043, -27.634058, 8],
            [153.0141011, -27.4797838, 8]
            
        ],
        columns = ["lon", "lat", "height"]
    )

    
    '''{
        "lon": [153.0693872, 152.9693843, 153.0141015],
        "lat": [-27.4402576, -27.634058, -27.4797838],
    }'''
    chart_data
    
    manual_data
    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=-27.634,
            longitude=152.969,
            zoom=6,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
               'HexagonLayer',
               data=manual_data,
               get_position='[lon, lat]',
               radius=40,
               elevation_scale=5,
               elevation_range=[10,200],
               pickable=True,
               extruded=True,
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=manual_data,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=25,
            )
        ],
    ))

    
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
                format="%f%%",
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

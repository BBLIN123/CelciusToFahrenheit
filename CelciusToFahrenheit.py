from datetime import datetime, date, time
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
# import webbrowser

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def get_weather_data(lat, lon):
    # You can use any weather API of your choice here to get the weather data.
    # For the sake of this example, I'm simply returning a random temperature.
    return 20.0
    
# Define the on_click callback
def open_info(event):
    if event["type"] == "click":
        lon, lat = event["coordinate"]
        info = df[(df["lon"] == lon) & (df["lat"] == lat)]["info"].values[0]
        st.info(info)
        st.write(f"Clicked on: {info}")

def main():
    st.title('This is not Weather Temperature Converter')
    '''
    btn_refresh = st.button('Refresh')
    if btn_refresh:
        st.write('test')
        st.button = False
        st.write('after test')
        #st.experimental_rerun()
    '''
 
    chart_data = pd.DataFrame(
       np.random.randn(100, 3) / [50, 50, 1] * [1, 1, 30] + [-27.634, 152.969, 105],
       columns=['lat', 'lon', 'elevation'])
    manual_data = pd.DataFrame(
        [
            [153.0693972, -27.4402676, 200],
            [152.9693743, -27.633058, 40],
            [152.9673813, -27.634458, 2000],
            [153.0161000, -27.4797338, 8],
            [153.0653879, -27.4402376, 200],
            [152.9643848, -27.634858, 200],
            [152.9777777, -27.634058, 80],
            
        ],
        columns = ['lon', 'lat', 'elevation']
    )
    
    chart_elevations = chart_data['elevation']
    manual_elevations = manual_data['elevation'].tolist()
    
    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=-27.634,
            longitude=152.969,
            zoom=10,
            pitch=50,
        ),
        layers=[
            
            pdk.Layer(
               'HexagonLayer',
               data=chart_data,
               get_position='[lon, lat]',
               elevation=chart_elevations,
               radius=50,
               
               
               pickable=True,
               extruded=True,
               coverage=1,
            ),
            pdk.Layer(
               'HexagonLayer',
               data=manual_data,
               get_position='[lon, lat]',
               get_elevation='manual_elevations',
               radius=50,
               elevation_scale=5,
               
               pickable=True,
               extruded=True,
               coverage=1,
            ),
        ],
    ))

    '''
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
    
    pdk.Layer(
               'HexagonLayer',
               data=chart_data,
               get_position='[lon, lat]',
               get_elevation='chart_elevations',
               radius=50,
               elevation_scale=6,
               elevation_range=[100,500],
               pickable=True,
               extruded=True,
               coverage=1,
            ),
            '''

if __name__ == '__main__':
    main()

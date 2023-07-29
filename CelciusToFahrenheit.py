import streamlit as st
import streamlit.components.v1 as components
from streamlit_js_eval import streamlit_js_eval, copy_to_clipboard, create_share_link, get_geolocation
import json, os

absolute_path = os.path.dirname(os.path.abspath(__file__))
frontend_path = absolute_path

streamlit_js_eval = components.declare_component(
    "streamlit_js_eval",
    path=frontend_path
)

def set_cookie(name, value, duration_days, component_key=None):
    js_ex = f'setCookie(\'{name}\', \'{value}\', {duration_days})'
    if component_key is None: component_key=js_ex
    return streamlit_js_eval(js_expressions=js_ex, key = component_key )

def get_cookie(name, component_key=None):
    if component_key is None: component_key=f'getCookie_{name}'
    return streamlit_js_eval(js_expressions=f'getCookie(\'{name}\')', key = component_key)

def get_user_agent(component_key=None):
    if component_key is None: component_key='UA'
    return streamlit_js_eval(js_expressions=f'window.navigator.userAgent', key = component_key)

def copy_to_clipboard(copiedText, linkText, successText, component_key=None):
    js_text = ''' 
    setFrameHeight(100);
    document.getElementsByTagName("body")[0].innerHTML += `<a href="#%s" id="cbc" rel="noopener noreferrer">%s</a>`;
    
    document.getElementById("cbc").addEventListener("click", function() {
        console.log('Copying')
        const copiedText = `%s`
        copyToClipboard(copiedText, () => document.getElementById("cbc").innerHTML = '%s' );
        
      })
    '''%(str(87264), linkText, copiedText, successText)
    if component_key is None: component_key=f'{linkText}{copiedText}{successText}'
    return streamlit_js_eval(js_expressions=js_text, key = component_key)

def get_geolocation(component_key=None):
    js_text = 'getLocation()' 
    if component_key is None: component_key=js_text
    return streamlit_js_eval(js_expressions=js_text, key = component_key)

def get_browser_language(component_key=None):
    if component_key is None: component_key='LANG'
    return streamlit_js_eval(js_expressions=f'window.navigator.language', key = component_key)

def get_page_location(component_key=None):
    if component_key is None: component_key='LOC'
    return json.loads(streamlit_js_eval(js_expressions='JSON.stringify(window.location)', key = component_key))


def create_share_link(sharedObject, linkText, successText, component_key=None):
    js_text = ''' 
    setFrameHeight(100);
    document.getElementsByTagName("body")[0].innerHTML += `<a href="#%s" id="shli">%s</a>`;
    
    document.getElementById("shli").addEventListener("click", function() {
        console.log('Sharing')
        if (navigator.share) {
            navigator.share(%s).then(() => {
            document.getElementById("shli").innerHTML = '%s'
            console.log('Thanks for sharing!');
        })
        .catch(console.error);
        } else {
           console.log('Sharing failed')
        }
      })
    '''%(str(87264), linkText, sharedObject, successText)
    
    if component_key is None: component_key=f'{linkText}{sharedObject}{successText}'

    return streamlit_js_eval(js_expressions=js_text, key = component_key)
#-----------------------------------------------------------
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def get_weather_data(lat, lon):
    # You can use any weather API of your choice here to get the weather data.
    # For the sake of this example, I'm simply returning a random temperature.
    return 20.0

st.write(f"User agent is _{streamlit_js_eval(js_expressions='window.navigator.userAgent', want_output = True, key = 'UA')}_")

st.write(f"Screen width is _{streamlit_js_eval(js_expressions='screen.width', want_output = True, key = 'SCR')}_")

st.write(f"Browser language is _{streamlit_js_eval(js_expressions='window.navigator.language', want_output = True, key = 'LANG')}_")

st.write(f"Page location is _{ streamlit_js_eval(js_expressions='window.location.origin', want_output = True, key = 'LOC')}_")

# Copying to clipboard only works with a HTTP connection

copy_to_clipboard("Text to be copied!", "Copy something to clipboard (only on HTTPS)", "Successfully copied" , component_key = "CLPBRD")

# Share something using the sharing API
# create_share_link(dict({'title': 'streamlit-js-eval', 'url': 'https://github.com/aghasemi/streamlit_js_eval', 'text': "A description"}), "Share a URL (only on mobile devices)", 'Successfully shared', component_key = 'shdemo')
                
if st.checkbox("Check my location"):
    loc = get_geolocation()
    st.write(f"Your coordinates are {loc}")
    
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

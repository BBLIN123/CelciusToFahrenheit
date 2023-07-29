import streamlit as st

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    st.title('Celsius to Fahrenheit Converter')
    
    # Input Celsius temperature
    celsius_temp = st.number_input('Enter Celsius temperature:', value=0.0)

    # Convert Celsius to Fahrenheit
    fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)

    # Display the result
    st.write(f'{celsius_temp:.2f} Celsius is equal to {fahrenheit_temp:.2f} Fahrenheit')

if __name__ == '__main__':
    main()
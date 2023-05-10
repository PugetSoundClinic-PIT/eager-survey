import streamlit as st
import requests
import pandas as pd

# Define the base URL for the GH request - we will use this to append the user provided GH handle
url = "https://api.github.com/users/"

# Define the Streamlit app layout and inputs
st.sidebar.title("Find my repositories")
get_args = st.sidebar.text_input("Github Username")
send_get = st.sidebar.button("Search")

# Function to send the GET request and process the response as a table to display (not sure my response is defined correctly)
def send_request(get_args):
    res = requests.get(f"{url}{get_args}{/repos}")
    response_content = res.json()
    st.write("Raw Response:")
    st.write(response_content)

    if 'args' in response_content:
        response_args = response_content['args']
        st.write("Table:")
        st.write(pd.DataFrame(response_args.items(), columns=["Key", "Value"]))

# Send the GET request and display the response when the Send button is clicked
if send_get:
    send_request(get_args)

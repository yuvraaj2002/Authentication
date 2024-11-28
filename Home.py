import streamlit as st
import os
from streamlit_google_auth import Authenticate

# Load credentials from environment variables
client_credentials = {
    "web": {
        "client_id": os.getenv("CLIENT_ID"),
        "project_id": os.getenv("PROJECT_ID"),
        "auth_uri": os.getenv("AUTH_URI"),
        "token_uri": os.getenv("TOKEN_URI"),
        "auth_provider_x509_cert_url": os.getenv("CERT_URL"),
        "client_secret": os.getenv("CLIENT_SECRET"),
        "redirect_uris": [os.getenv("REDIRECT_URI")],
    }
}

st.title('Streamlit Google Auth Example')

if 'connected' not in st.session_state:
    # Pass the credentials dictionary instead of JSON file
    authenticator = Authenticate(
        secret_credentials_dict=client_credentials,  # Use the dictionary here
        cookie_name='my_cookie_name',
        cookie_key='this_is_secret',
        redirect_uri=os.getenv("REDIRECT_URI"),
    )
    st.session_state["authenticator"] = authenticator

# Catch the login event
st.session_state["authenticator"].check_authentification()

# Create the login button
st.session_state["authenticator"].login()

if st.session_state['connected']:
    st.image(st.session_state['user_info'].get('picture'))
    st.write('Hello, '+ st.session_state['user_info'].get('name'))
    st.write('Your email is '+ st.session_state['user_info'].get('email'))
    
    if st.button('Log out'):
        st.session_state["authenticator"].logout()
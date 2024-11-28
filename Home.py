import streamlit as st
from streamlit_google_auth import Authenticate

# Load credentials from Streamlit secrets
client_credentials = {
    "web": {
        "client_id": st.secrets["google_credentials"]["client_id"],
        "project_id": st.secrets["google_credentials"]["project_id"],
        "auth_uri": st.secrets["google_credentials"]["auth_uri"],
        "token_uri": st.secrets["google_credentials"]["token_uri"],
        "auth_provider_x509_cert_url": st.secrets["google_credentials"]["cert_url"],
        "client_secret": st.secrets["google_credentials"]["client_secret"],
        "redirect_uris": st.secrets["google_credentials"]["redirect_uris"],
    }
}

st.title('Streamlit Google Auth Example')

if 'connected' not in st.session_state:
    # Pass the credentials dictionary to the authenticator
    authenticator = Authenticate(
        secret_credentials_dict=client_credentials,  # Use the dictionary here
        cookie_name='my_cookie_name',
        cookie_key='this_is_secret',
        redirect_uri=st.secrets["google_credentials"]["redirect_uris"][0],  # Use the first redirect URI
    )
    st.session_state["authenticator"] = authenticator

# Catch the login event
st.session_state["authenticator"].check_authentification()

# Create the login button
st.session_state["authenticator"].login()

# Display user info if logged in
if st.session_state['connected']:
    st.image(st.session_state['user_info'].get('picture'))
    st.write('Hello, ' + st.session_state['user_info'].get('name'))
    st.write('Your email is ' + st.session_state['user_info'].get('email'))

    if st.button('Log out'):
        st.session_state["authenticator"].logout()

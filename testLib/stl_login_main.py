import pickle
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st
import streamlit_authenticator as stauth

st.set_page_config(page_title='Login to your account', layout='wide')

name = ["Anh Tran"]
username = ["anhtran"]

file_path = Path(__file__).parent / "hash_pw.pkl"
with open(file_path, "rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(name, username, hashed_passwords,
                                    "Login_account", "abcdef", cookie_expiry_days=30)

name, authenticator_status, username = authenticator.login("Login", "main")

if authenticator_status == False:
    st.error("Username or Password is incorrect")

if authenticator_status == None:
    st.warning("Please enter your username and password")

if authenticator_status:
    st.balloons()
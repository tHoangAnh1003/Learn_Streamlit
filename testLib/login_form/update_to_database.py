import streamlit_authenticator as stauth

import database as db

name = ['Anh Tran', 'ABC']
username = ['anhtran', 'abc']
password = ['123456', '123456']

hashed_passwords = stauth.Hasher(password).generate()  # Hash password

for (username, name, hash_password) in zip(username, name, hashed_passwords):
    db.insert_user(username, name, hash_password)
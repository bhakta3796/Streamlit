import streamlit as st

email = st.text_input('Enter email')
password = st.text_input('Enter password')
gender = st.selectbox('select gender', ['male', 'female', 'others'])

btn = st.button('login')

if btn:
    if email == 'bhaktadebasis340@gmail.com' and password == '1234':
        st.success('login successful')
        st.balloons()
        st.write(gender)
    else:
        st.error('login failed')
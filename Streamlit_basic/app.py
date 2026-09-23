import streamlit as st
import pandas as pd
import time

st.title('Startup Dashboard')
st.header('I am learning Streamlit')
st.subheader('Arijit')

st.write('This is normal text')

st.markdown("""
    ### my fevorite movies
    - Sutter iland
    - Identity
    - Catch me if you can 
""")

st.code("""
    def fun(n):
        return n ** 2

    x = fun(3)
    print(x)
""")

st.latex('x^2 + y^2 = 6')

df = pd.DataFrame({
    'name' : ['Debasis', 'Arijit', 'Anshu'],
    'marks' : [50, 60, 70],
    'package' : [10, 12, 14]
})

st.dataframe(df)

st.metric('Revenue', 'Rs 3L', '3')

st.json({
        'name' : ['Debasis', 'Arijit', 'Anshu'],
    'marks' : [50, 60, 70],
    'package' : [10, 12, 14]
})

st.image('image.png')

st.sidebar.title('sidebar item') 

col1, col2 = st.columns(2)

with col1:
    st.image('image.png')

with col2:
    st.image('image.png')

st.error('login failed')

st.success('login successful')

bar = st.progress(0)

for i in range(1, 100):
    time.sleep(0.1)
    bar.progress(i)

email = st.text_input('Enter email')
number = st.number_input('Enter age')
st.date_input('Enter date')
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout = 'wide')

df = pd.read_csv('india.csv')

list_of_states = list(df['State'].unique())

list_of_states.insert(0, 'Overall India')

st.sidebar.title('India Data Visulation')
selected_state = st.sidebar.selectbox('Select a State', list_of_states)

x = sorted(df.columns[5:])
primary = st.sidebar.selectbox('Select Primary Parameter', x)

secondary = st.sidebar.selectbox('Select Secondary Parameter', x)

plot = st.sidebar.button('Plot Graph')

if plot:

    st.text('Size represent primary parameter')
    st.text('Color represent secondary parameter')
    
    if selected_state == 'Overall India':
        # plot for india
        fig = px.scatter_map(df, lat = "Latitude", lon = "Longitude", zoom = 3, size_max = 35,
                             map_style = 'open-street-map', height = 580, width = 1200,
                             size = primary, color = secondary, color_continuous_scale="Turbo",
                             hover_name = 'District'                             
                            )

        st.plotly_chart(fig, use_container_width = True)

    else:
        # plot for state
        state_df = df[df['State'] == selected_state]

        fig = px.scatter_map(state_df, lat = "Latitude", lon = "Longitude", zoom = 6, size_max = 35,
                             map_style = 'open-street-map', height = 580, width = 1200,
                             size = primary, color = secondary, color_continuous_scale="Turbo",
                             hover_name = 'District'                            
                            )

        st.plotly_chart(fig, use_container_width = True)

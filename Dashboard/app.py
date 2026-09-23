import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide', page_title='Startup Analysis')    

df = pd.read_csv('startup_cleaned.csv')


def load_overall_analysis():
    st.title('Overall Analysis')

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        # total invested amount
        total = round(df['amount'].sum())
        st.metric('Total Invested Amount', str(total) + ' Cr')

    with col2:
        # max amount infused in a startup
        max_funding = df['amount'].max()
        st.metric('Max Invested Amount', str(max_funding) + 'Cr')

    with col3:
        # avg amount 
        avg = round(df['amount'].mean())
        st.metric('Average Invested Amount', str(avg) + ' Cr')

    with col4:
        # total funded startup
        startup = df['startup'].nunique()
        st.metric('Total Funded Startups', str(startup))

df['date'] = pd.to_datetime(df['date'], errors = 'coerce')

def load_investor_details(investor):
    st.title(investor)

    # load the resent 5 investments of the investor
    st.subheader('Most resent Investments')
    last5_df = df[df['investors'].str.contains(investor)].head()[['date','startup','vertical','city','round','amount']]
    st.dataframe(last5_df)

    col1, col2 = st.columns(2)
    with col1:
        # biggest investments
        st.subheader('Biggest Investments')
        big_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head(6)
        fig,ax = plt.subplots()
        ax.bar(big_series.index, big_series.values)
        st.pyplot(fig)

    with col2:
        vertical_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head(6)
        st.subheader('Biggest Investments')
        st.dataframe(vertical_series)

    col1, col2 = st.columns(2)
    with col1:
        vertical_series = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum().sort_values(ascending=False).head(6)
        st.subheader('Sectors Invested in')
        fig1,ax1 = plt.subplots()
        ax1.pie(vertical_series, labels=vertical_series.index, autopct="%0.01f%%")
        st.pyplot(fig1)

    with col2:
        city_series = df[df['investors'].str.contains(investor)].groupby('city')['amount'].sum().sort_values(ascending=False).head(6)
        st.subheader('Citys Invested')
        fig2,ax2 = plt.subplots()
        ax2.pie(city_series, labels=city_series.index, autopct="%0.01f%%")
        st.pyplot(fig2)

    df['year'] = df['date'].dt.year

    year_series = (
        df[df['investors'].str.contains(investor, na=False)]
        .groupby('year')['amount']
        .sum()
    )

    st.subheader('Year On Year Investment')

    fig3, ax3 = plt.subplots()

    if year_series.empty or year_series.sum() == 0:
        ax3.text(
            0.5,
            0.5,
            "No investment data available",
            ha="center",
            va="center"
        )
        ax3.axis("off")
    else:
        ax3.plot(
            year_series.index,
            year_series.values,
            marker='o'
        )

        ax3.set_xlabel("Year")
        ax3.set_ylabel("Investment Amount")
        ax3.set_title("Year On Year Investment")

        ax3.grid(True)

    st.pyplot(fig3)


st.sidebar.title('startup funding analysis')

option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'Investor'])

if option == 'Overall Analysis':
    btn0 = st.sidebar.button('Show Overall Analysis')

    if btn0:
        load_overall_analysis()

# elif option == 'Startup':
#     st.sidebar.selectbox('Select Startup',sorted(list(df['startup'].unique())))
#     btn1 = st.sidebar.button('find startup details')
#     st.title('Startup Analysis')

else:
    selected_investor = st.sidebar.selectbox('Select Investor',sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('find investors')
    st.title('Investor Analysis')

    if btn2:
        load_investor_details(selected_investor)

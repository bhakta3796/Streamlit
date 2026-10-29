import pandas as pd
import streamlit as st

matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

st.title("🏏 IPL Analytics Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Matches", matches.shape[0])

with col2:
    st.metric("Total Teams", pd.unique(
        pd.concat([matches["team1"], matches["team2"]])
    ).size)

with col3:
    st.metric("Total Runs", deliveries["total_runs"].sum())

team_wins = (
    matches["winner"].value_counts().reset_index()
)

team_wins.columns = ["Team", "Wins"]

team_wins = team_wins.sort_values(
    "Wins",
    ascending=False
)

st.subheader("Most Successful IPL Teams")

st.bar_chart(
    team_wins,
    x="Team",
    y="Wins"
)
import streamlit as st # load streamlit library and call it st
st.title("Football Analysis") # show a big title on the web page
st.caption("Data from public sources (league stats only, season 2025/26; Messi: MLS 2025). It may contain small errors.") # small grey note under the title
import pandas as pd # load the pandas library and call it pd
df =pd.read_csv("players.csv") # read the players file into a table called df
league_choice = st.sidebar.selectbox("choose a league", df["league"].unique()) # league list in the sidebar
league_df = df[df["league"] == league_choice] # keep only players of the chosen league
st.dataframe(league_df) # show only the chosen league's players
selected = st.selectbox("choose a player", league_df["name"]) # dropdown list with  players of the chosen league 
player = df[df["name"] == selected] # keep only the row of the chosen player
st.dataframe(player) # show the chosen player's row on the web page
club_colors = {  # dictionary: club name -> its colour code
    "Inter Miami": "#F7B5CD",
    "Barcelona": "#004D98",
    "Real Madrid": "#FFFFFF",
    "Man City": "#6CABDD",
    "Bayern Munich": "#DC052D",
    "Inter": "#0B2A6F",
    "PSG": "#004170",
}
club = player["club"].iloc[0]  # club name of the chosen player (first and only row)
color = club_colors[club]  # look up the club colour in the dictionary
text_color = "black" if club in ["Real Madrid", "Inter Miami", "Man City"] else "white"  # dark text on light colours
st.markdown(f'<div style="background-color:{color}; color:{text_color}; padding:12px; border-radius:8px; text-align:center; font-size:24px; border:1px solid #999;">{club}</div>', unsafe_allow_html=True)  # show the club name in a coloured box
goals = player["goals"].iloc[0]  # goals of the chosen player
matches = player["matches"].iloc[0]  # matches of the chosen player
col1, col2, col3 = st.columns(3)  # create three columns side by side
col1.metric("Goals", goals)  # big number card in the first column
col2.metric("Matches", matches)  # big number card in the second column
col3.metric("Goals per match", round(goals / matches, 2))  # goals divided by matches, rounded to 2 decimals
import matplotlib.pyplot as plt # load the matplotlib library for charts
fig = plt.figure() # create an empty figure to draw the chart on
plt.bar(league_df["name"], league_df["goals"]) # draw one bar per player: names on x axis, goals on y axis
plt.title("goals per player") # title shown above the chart
st.pyplot(fig) # show the chart on the web page
fig2 = plt.figure() # create a second empty figure for the scatter chart
plt.scatter(league_df["matches"], league_df["goals"]) # one dot per player: matches on x axis, goals on y axis
plt.title("goals vs matches") # title shown above the chart
plt.xlabel("matches") # name of the horizontal axis
plt.ylabel("goals") # name of the vertical axis
st.pyplot(fig2) # show the second chart on the web page
import streamlit as st # load streamlit library and call it st
st.title("Football Analysis") # show a big title on the web page
import pandas as pd # load the pandas library and call it pd
df =pd.read_csv("players.csv") # read the players file into a table called df
st.dataframe(df) # show the table on the web page
selected = st.selectbox("choose a player", df["name"]) # dropdown list with all player names
player = df[df["name"] == selected] # keep only the row of the chosen player
st.dataframe(player) # show the chosen player's row on the web page
import matplotlib.pyplot as plt # load the matplotlib library for charts
fig = plt.figure() # create an empty figure to draw the chart on
plt.bar(df["name"], df["goals"]) # draw one bar per player: names on x axis, goals on y axis
plt.title("goals per player") # title shown above the chart
st.pyplot(fig) # show the chart on the web page
fig2 = plt.figure() # create a second empty figure for the scatter chart
plt.scatter(df["matches"], df["goals"]) # one dot per player: matches on x axis, goals on y axis
plt.title("goals vs matches") # title shown above the chart
plt.xlabel("matches") # name of the horizontal axis
plt.ylabel("goals") # name of the vertical axis
st.pyplot(fig2) # show the second chart on the web page
import streamlit as st

from functions.plotly_ts import plot
st.title("mrzada begin")
st.write("in the house")
ticker = st.sidebar.text_input("escolha o ticker",value = "AAPL")
fig = plot(ticker)
st.plotly_chart(fig)
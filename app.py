import streamlit as st

from functions.plotly_ts import plot
st.title("Histórico de cotações")
st.write("Veja o histórico")
ticker = st.sidebar.text_input("escolha o ticker",value = "AAPL")
fig = plot(ticker)
st.plotly_chart(fig)
st.image("images/QRCode_Fácil (1).png")
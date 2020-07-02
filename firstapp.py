import streamlit as st
import yfinance as yf 
import pandas as pd 

st.write("""
## Simple stock price App
by akash a desai \n

shows ***stock*** closing and volue of **price**

""")



tickerSymbol='GOOGL'

tickerData=yf.Ticker(tickerSymbol)

tickerDf=tickerData.history(period='1d',start="2010-5-31",end='2020-5-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
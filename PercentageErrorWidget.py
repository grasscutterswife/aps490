import streamlit as st

#values of observed, true and percentage error
observedNumber = float("1.25")
trueNumber= float("2")
calculate = float((trueNumber -observedNumber)/trueNumber)*100


#Percentage Error Widget
col1, col2, col3 = st.columns(3)
col1.metric('Observed Value', value= observedNumber)
col2.metric('True Value', value = trueNumber)
col3.metric('Percentage Error', value = calculate)

    

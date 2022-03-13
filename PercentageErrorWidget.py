import streamlit as st

#Percentage Error Widget
observedNumber = st.number_input('Observed Value')
trueNumber = st.number_input('True Value')
erroePercentage =st.number_input('Percentage Error',step = percentage_of_error)

def percentage_of_error:
    calculate = float(observedNumber/trueNumber)*100
    
    

import streamlit as st
import random
import matplotlib.pyplot as plt

# x axis values
x = [1,2,3]
# corresponding y axis values
y = [2,4,1]
 
# plotting the points
fig = plt.plot(x, y)

# Frame plotting into values
def load_data(nrows):
    data =pd.plotting(fig, nrows=nrows)
    data.remname(axis ='y',inplace = True)
    data['x']=pd.to_datatime(data["x"])
    return data
   
#Create the Frame
#The widgets for selection
st.dataframe(data, height=2000)
st.selectbox('Select Variable', range("Air Flow","Valve Position"))
st.selectbox('Select unit',range(1,43))
st.selectbox('Select month',range(1,12))
st.selectbox('Select day',range(0,31))
st.subheader('Data Alert for %sh' % y)
st.write(data)

@st.cache
def convert_data(data):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return data.to_csv().encode("Alerts")

#Download button
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name="alert.csv",
    mime="text/csv",
)



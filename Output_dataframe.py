import streamlit as st
import random
import matplotlib.pyplot as plt
# x axis values
x = [1,2,3]
# corresponding y axis values
y = [2,4,1]
 
# plotting the points
fig = plt.plot(x, y)

def load_data(nrows):
    data =pd.plotting(fig, nrows=nrows)
    data.remname(axis ='y',inplace = True)
    data['x']=pd.to_datatime(data["x"])
    data[outlier_dates]=df.style.highlight_max(axis= 'y'))
    return data

data =load_data[1000]
st.selectbox('Select date',range(1,12))
st.selectbox('Select hour', range(0,24))

st.subheader('Data Alert for %sh' % y)
st.write(data)

import streamlit as st

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

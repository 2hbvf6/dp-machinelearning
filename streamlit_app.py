import streamlit as st
import pandas as pd

st.title('🤖 Machine Laerning App')

st.write('This ia app builds machine learning models !')

with st.expander('Data'):
  st.write('**Raw Data**')
  df= pd.read_csv(' https://raw.githubusercontent.com/2hbvf6/dp-machinelearning/refs/heads/master/Updated%20data_01_05_2025.csv ')
  df

st.write('**X**')
X = df.drop('label' , axis=1)
X 
st.write('**Y**')
Y = df.label
Y

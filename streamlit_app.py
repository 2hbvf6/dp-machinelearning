import streamlit as st
import pandas as pd

st.title('🤖 Machine Laerning App')

st.write('This ia app builds machine learning models !')
with st.expander('Data'):
  st.write('**Raw Data**')
  df= pd.read_csv(' C:\Users\sahai\OneDrive\Desktop\habuda project\updated exel.csv.xlsx ')
  df

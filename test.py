import streamlit as st
import pandas as pd

st.title('My First StreamLit Web App')

df= pd.DataFrame({"one":[1,2,3],"two":[4,5,6],"three":[7,8,9]})
st.write(df)

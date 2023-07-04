import streamlit as st
import pandas as pd
import numpy as np
# import plotly.express as px

def format_page():
    st.title("Wgeather Forecast for the Next Days")
    st.text_input("Place",help="HEy")
    st.slider("Forecast Days",0,5, help="HEy")
    st.selectbox("Select data to view",("Temperature","Sky"),help="HEy")

    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.line_chart(chart_data)
if __name__ == '__main__':
    format_page()
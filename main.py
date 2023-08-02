import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search for Happiness")
options_x = st.selectbox("Select the data for the X-axis", ("GDP", "Happiness", "Generosity"))
options_y = st.selectbox("Select the data for the Y-axis", ("GDP", "Happiness", "Generosity"))
st.subheader(f"{options_x} and {options_y}")


df = pd.read_csv("data/happy.csv")
match options_x:
    case "GDP":
        data_x = df["gdp"]
    case "Happiness":
        data_x = df["happiness"]
    case "Generosity":
        data_x = df["generosity"]

match options_y:
    case "GDP":
        data_y = df["gdp"]
    case "Happiness":
        data_y = df["happiness"]
    case "Generosity":
        data_y = df["generosity"]

figure = px.scatter(x=data_x, y=data_y, labels={"x": options_x, "y": options_y})
st.plotly_chart(figure)

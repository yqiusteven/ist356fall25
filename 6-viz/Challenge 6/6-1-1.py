import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


mobile = pd.read_csv("./6-viz/data/mobile_user_behavior_dataset.csv")

st.title("Mobile User Behavior Analysis")
st.dataframe(mobile)

col1, col2 = st.columns(2)
category = col1.selectbox("Select a category:", ["Gender", "Operating System"])
measure = col2.selectbox("Select a measure:", ["Data Usage (MB/day)", "Battery Drain (mAh/day)", "Screen On Time (hours/day)", "App Usage Time (min/day)"])

figure, series = plt.subplots()
sns.barplot(data=mobile, x=category, y=measure, hue=category, estimator='mean', ax=series)
st.pyplot(figure)
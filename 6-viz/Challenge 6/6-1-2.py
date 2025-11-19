import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


mobile = pd.read_csv("./6-viz/data/mobile_user_behavior_dataset.csv")
st.dataframe(mobile)

st.subheader("Age vs Data Usage")
figure1, series1 = plt.subplots()
sns.lineplot(data=mobile, x="Age", y="Data Usage (MB/day)", estimator="mean", ax=series1, errorbar=None)
st.pyplot(figure1)
st.subheader("Age vs Data Usage by Gender")
figure2, series2 = plt.subplots()
sns.lineplot(data=mobile, x="Age", y="Data Usage (MB/day)", hue="Gender", estimator="mean", ax=series2, errorbar=None)
st.pyplot(figure2)
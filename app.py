import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Universitario", layout="wide")

df = pd.read_csv("university_student_data.csv")

st.title("📊 Dashboard Analítico de Estudiantes Universitarios")

year = st.selectbox("Seleccionar Año:", sorted(df['Year'].unique()))
term = st.selectbox("Seleccionar Periodo:", sorted(df['Term'].unique()))

filtered_df = df[(df['Year'] == year) & (df['Term'] == term)]

st.metric("Estudiantes Matriculados", int(filtered_df['Enrolled'].sum()))
st.metric("Tasa de Retención (%)", float(filtered_df['Retention Rate (%)'].mean()))
st.metric("Satisfacción (%)", float(filtered_df['Student Satisfaction (%)'].mean()))

fig1, ax1 = plt.subplots()
ax1.plot(df.groupby('Year')['Retention Rate (%)'].mean(), marker='o')
ax1.set_title("Tendencia de Retención")
st.pyplot(fig1)

fig2, ax2 = plt.subplots()
ax2.bar(df['Year'].unique(), df.groupby('Year')['Student Satisfaction (%)'].mean())
ax2.set_title("Satisfacción Promedio por Año")
st.pyplot(fig2)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración Inicial
st.set_page_config(page_title="Dashboard Universitario", layout="wide")

# Cargar datos
df = pd.read_csv("university_student_data.csv")


st.title("📊 Dashboard Analítico de Estudiantes Universitarios")

# Filtros Interactivos
col1, col2 = st.columns(2)

with col1:
    year = st.selectbox("Seleccionar Año:", sorted(df['Year'].unique()))

with col2:
    term = st.selectbox("Seleccionar Periodo:", sorted(df['Term'].unique()))

# Filtrar los datos según selección
filtered_df = df[(df['Year'] == year) & (df['Term'] == term)]

# Métricas Clave
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Estudiantes Matriculados", int(filtered_df['Enrolled'].sum()))

with col2:
    st.metric("Tasa de Retención (%)", float(filtered_df['Retention Rate (%)'].mean()))

with col3:
    st.metric("Satisfacción (%)", float(filtered_df['Student Satisfaction (%)'].mean()))

# GRÁFICO 1: TENDENCIA DE RETENCIÓN (DINÁMICO)

st.subheader("📈 Tendencia de Retención a lo Largo del Tiempo")

retention_trend = df.groupby('Year')['Retention Rate (%)'].mean()

fig1, ax1 = plt.subplots()
ax1.plot(retention_trend.index, retention_trend.values, marker='o', color='blue')
ax1.set_xlabel("Año")
ax1.set_ylabel("Tasa de Retención (%)")
ax1.set_title("Tendencia de Retención")
st.pyplot(fig1)

# GRÁFICO 2: SATISFACCIÓN PROMEDIO POR AÑO (DINÁMICO)
st.subheader("Satisfacción Promedio por Año")

satisfaction_trend = df.groupby('Year')['Student Satisfaction (%)'].mean()

fig2, ax2 = plt.subplots()
ax2.bar(satisfaction_trend.index, satisfaction_trend.values, color='orange')
ax2.set_xlabel("Año")
ax2.set_ylabel("Satisfacción (%)")
ax2.set_title("Satisfacción Promedio por Año")
st.pyplot(fig2)

# GRÁFICO 3: COMPARACIÓN ENTRE SPRING Y FALL (DINÁMICO)
st.subheader(" Comparación entre Periodos Spring y Fall")

term_comparison = df[df['Year'] == year].groupby('Term')[['Retention Rate (%)', 'Student Satisfaction (%)']].mean()

fig3, ax3 = plt.subplots()
term_comparison.plot(kind='bar', ax=ax3, color=['green', 'purple'])
ax3.set_xlabel("Periodo Académico")
ax3.set_ylabel("Porcentaje (%)")
ax3.set_title(f"Comparación entre Spring y Fall - Año {year}")
ax3.grid(axis='y')
st.pyplot(fig3)

st.caption("Todos los indicadores y gráficos se actualizan dinámicamente según el año y el periodo seleccionados.")

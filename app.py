import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Universitario", layout="wide")
st.title("📊 Dashboard Analítico de Estudiantes Universitarios")

df = pd.read_csv("university_student_data.csv")

# filtros interactivos
col1, col2 = st.columns(2)

with col1:
    year = st.selectbox("Seleccionar Año:", sorted(df['Year'].unique()))

with col2:
    term = st.selectbox("Seleccionar Periodo:", sorted(df['Term'].unique()))

# Filtrar los datos según la selección
filtered_df = df[(df['Year'] == year) & (df['Term'] == term)]


# métricas clave
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Estudiantes Matriculados", int(filtered_df['Enrolled'].sum()))

with col2:
    st.metric("Tasa de Retención (%)", round(filtered_df['Retention Rate (%)'].mean(), 1))

with col3:
    st.metric("Satisfacción (%)", round(filtered_df['Student Satisfaction (%)'].mean(), 1))


# gráfico 1: retención en el año seleccionado
st.subheader(f"📈 Retención por Departamento - {year} / {term}")

dept_cols = ['Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled', 'Science Enrolled']

fig1, ax1 = plt.subplots()
ax1.bar(dept_cols, filtered_df[dept_cols].values[0], color=['royalblue', 'orange', 'green', 'purple'])
ax1.set_ylabel("Estudiantes Matriculados")
ax1.set_title("Distribución de Matrícula por Departamento")
st.pyplot(fig1)

# gráfico 2: tendencia de retención en los años
st.subheader("📊 Tendencia de Retención en el Tiempo")

# Mostrar tendencia solo del periodo seleccionado (Spring/Fall)
retention_trend = df[df['Term'] == term].groupby('Year')['Retention Rate (%)'].mean()

fig2, ax2 = plt.subplots()
ax2.plot(retention_trend.index, retention_trend.values, marker='o', color='blue')
ax2.set_xlabel("Año")
ax2.set_ylabel("Tasa de Retención (%)")
ax2.set_title(f"Tendencia de Retención - Periodo {term}")
st.pyplot(fig2)

# gráfico 3: satisfacción promedio (diferencia entre periodos)
st.subheader(" Comparación de Satisfacción entre Spring y Fall")

satisfaction_compare = df[df['Year'] == year].groupby('Term')['Student Satisfaction (%)'].mean()

fig3, ax3 = plt.subplots()
ax3.bar(satisfaction_compare.index, satisfaction_compare.values, color=['skyblue', 'salmon'])
ax3.set_xlabel("Periodo")
ax3.set_ylabel("Satisfacción (%)")
ax3.set_title(f"Comparación de Satisfacción en {year}")
st.pyplot(fig3)

st.caption("Todos los gráficos e indicadores se actualizan dinámicamente según el año y periodo seleccionados.")

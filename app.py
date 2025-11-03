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
st.subheader(f"🎓 Estudiantes Matriculados por Departamento  - {year} / {term}")

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

# gráfico 3: circular por departamento
st.subheader(f"📊 Distribución Porcentual de Matrícula por Departamento - {year} / {term}")

dept_enroll = [
    filtered_df['Engineering Enrolled'].sum(),
    filtered_df['Business Enrolled'].sum(),
    filtered_df['Arts Enrolled'].sum(),
    filtered_df['Science Enrolled'].sum()
]

dept_labels = ['Engineering', 'Business', 'Arts', 'Science']

fig3, ax3 = plt.subplots()
ax3.pie(
    dept_enroll,
    labels=dept_labels,
    autopct='%1.1f%%',
    startangle=90,
    colors=['#4e79a7', '#f28e2b', '#59a14f', '#8b3fc6']
)
ax3.set_title("Distribución Porcentual de Matrícula")
ax3.axis('equal')  # Hace que el gráfico sea circular y no ovalado

# Mostrar gráfico en Streamlit
st.pyplot(fig3)
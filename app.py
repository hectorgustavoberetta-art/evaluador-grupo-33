import streamlit as st
import tempfile
from agente.evaluador import evaluar_trabajo
st.set_page_config(
    page_title="Agente Evaluador - Grupo 33",
    page_icon="🎓",
    layout="wide"
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #f2f2f2;
    }
    </style>
    """,
    unsafe_allow_html=True
)

col_titulo, col_logo = st.columns([4, 1])

with col_titulo:
    st.title("Agente Evaluador - Grupo 33")
    st.subheader("MBA UCEMA · Programación de y con Agentes de IA")

with col_logo:
    st.image("assets/Logo_UCEMA.png", width=180)

st.markdown(
    """
    Esta aplicación permite cargar uno o varios trabajos académicos,
    evaluarlos mediante una rúbrica ejecutable y generar una devolución
    objetiva, consistente y trazable.
    """
)

st.divider()

st.header("1. Cargar trabajos")

archivos = st.file_uploader(
    "Seleccioná uno o varios trabajos para evaluar",
    type=["md", "txt", "py", "json"],
    accept_multiple_files=True
)

if archivos:
    st.success(f"Trabajos cargados: {len(archivos)}")

    for archivo in archivos:
        st.write(f"• {archivo.name}")

st.divider()

st.header("2. Evaluación")

st.info(
    "El agente realizará primero el control de fraude y luego aplicará "
    "la rúbrica académica correspondiente."
)

boton_evaluar = st.button(
    "Evaluar trabajos",
    type="primary",
    disabled=not archivos
)

if boton_evaluar:
    for archivo in archivos:
        st.subheader(f"Evaluación de: {archivo.name}")

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=f"_{archivo.name}"
        ) as temporal:
            temporal.write(archivo.getvalue())
            ruta_temporal = temporal.name

        with st.spinner(f"Evaluando {archivo.name}..."):
            resultado = evaluar_trabajo(ruta_temporal)

        st.success(f"Evaluación completada: {archivo.name}")
        st.markdown(resultado)

        st.download_button(
            label=f"Descargar evaluación de {archivo.name}",
            data=resultado,
            file_name=f"{archivo.name}_evaluacion.md",
            mime="text/markdown",
            key=f"descarga_{archivo.name}"
        )

        st.divider()

st.divider()

st.caption(
    "Agente Evaluador · Grupo 33 · MBA UCEMA · 2026"
)


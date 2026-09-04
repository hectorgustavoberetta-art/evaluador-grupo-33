import streamlit as st
import tempfile
from agente.evaluador import evaluar_trabajo

st.set_page_config(
    page_title="Agente Evaluador - Grupo 33",
    page_icon="🎓",
    layout="wide"
)

# ---------------------------------------------------------
# ESTILO VISUAL
# ---------------------------------------------------------

st.markdown(
    """
    <style>
    .stApp {
        background-color: #f2f2f2;
    }

    div.stButton > button[kind="primary"] {
        background-color: #a90032;
        border-color: #a90032;
        color: white;
        font-weight: 700;
    }

    div.stButton > button[kind="primary"]:hover {
        background-color: #8c002a;
        border-color: #8c002a;
    }

    .panel {
        background-color: white;
        padding: 22px 26px;
        border-radius: 12px;
        border: 1px solid #e2e2e2;
        margin-bottom: 16px;
    }

    .panel h3 {
        margin-top: 0;
        color: #172b4d;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# ENCABEZADO
# ---------------------------------------------------------

col_titulo, col_logo = st.columns([4, 1])

with col_titulo:
    st.title("Agente Evaluador - Grupo 33")
    st.subheader("MBA UCEMA · Programación de y con Agentes de IA")
    st.write(
        "Esta aplicación permite cargar uno o varios trabajos académicos, "
        "evaluarlos mediante una rúbrica ejecutable y generar una devolución "
        "objetiva, consistente y trazable."
    )

with col_logo:
    st.image("assets/Logo_UCEMA.png", width=180)

st.divider()

# ---------------------------------------------------------
# ÁREA PRINCIPAL
# ---------------------------------------------------------

col_principal, col_info = st.columns([1.7, 1], gap="large")

with col_principal:

    st.header("📄 1. Cargar trabajos")

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

    st.header("⚙️ 2. Evaluar")

    st.info(
        "El agente realizará primero el control de fraude y luego aplicará "
        "la rúbrica académica correspondiente."
    )

    boton_evaluar = st.button(
        "▶ Evaluar trabajos",
        type="primary",
        disabled=not archivos,
        use_container_width=True
    )

with col_info:

    st.markdown(
        """
        <div class="panel">
        <h3>🎯 ¿Qué hace este agente?</h3>
        <p>✓ Aplica una rúbrica ejecutable.</p>
        <p>✓ Evalúa múltiples trabajos.</p>
        <p>✓ Realiza control de posibles casos de fraude.</p>
        <p>✓ Genera devoluciones detalladas y recomendaciones de mejora.</p>
        <p>✓ Permite descargar individualmente cada evaluación.</p>
        </div>

        <div class="panel">
        <h3>👥 Integrantes – Grupo 33</h3>
        <p>Héctor Gustavo Beretta</p>
        <p>Eliana Androszczuk</p>
        <p>Diego Gonzalez</p>
        <p>Agustin Poselski</p>
        </div>

        <div class="panel">
        <h3>ℹ️ Nota</h3>
        <p>
        Esta herramienta fue desarrollada como trabajo parcial de la materia
        Programación de y con Agentes de IA · MBA UCEMA 2026.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------------------------------------------------
# RESULTADOS
# ---------------------------------------------------------

if boton_evaluar:
    st.divider()
    st.header("Resultados de la evaluación")

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

st.caption(
    "Agente Evaluador · Grupo 33 · MBA UCEMA · 2026"
)

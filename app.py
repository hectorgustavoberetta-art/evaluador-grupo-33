import io
import json
import re
import tempfile
import urllib.request
import urllib.parse
import zipfile
from pathlib import Path

import streamlit as st

from agente.evaluador import evaluar_trabajo


MAX_ZIP_BYTES = 50 * 1024 * 1024

def descargar_repositorio_github(url):
    """
    Descarga un repositorio público de GitHub como archivo ZIP.
    Devuelve: (nombre_repositorio, datos_zip)
    """

    url = url.strip()

    parsed = urllib.parse.urlparse(url)

    if parsed.scheme not in ("http", "https") or parsed.netloc.lower() != "github.com":
        raise ValueError(
            "La dirección debe corresponder a un repositorio público de GitHub."
        )

    partes = [p for p in parsed.path.strip("/").split("/") if p]

    if len(partes) < 2:
        raise ValueError(
            "La dirección de GitHub no parece corresponder a un repositorio."
        )

    propietario = partes[0]
    repositorio = partes[1]

    if repositorio.endswith(".git"):
        repositorio = repositorio[:-4]

    api_url = (
        f"https://api.github.com/repos/"
        f"{propietario}/{repositorio}"
    )

    request_api = urllib.request.Request(
        api_url,
        headers={
            "User-Agent": "Agente-Evaluador-Grupo-33"
        }
    )

    try:
        with urllib.request.urlopen(request_api, timeout=20) as respuesta:
            datos_repo = json.loads(
                respuesta.read().decode("utf-8")
            )

    except Exception as error:
        raise ValueError(
            "No se pudo acceder al repositorio. "
            "Verificá que exista y sea público."
        ) from error

    rama = datos_repo.get("default_branch")

    if not rama:
        raise ValueError(
            "No se pudo identificar la rama principal del repositorio."
        )

    rama_codificada = urllib.parse.quote(
        rama,
        safe=""
    )

    zip_url = (
        f"https://codeload.github.com/"
        f"{propietario}/{repositorio}/zip/refs/heads/"
        f"{rama_codificada}"
    )

    request_zip = urllib.request.Request(
        zip_url,
        headers={
            "User-Agent": "Agente-Evaluador-Grupo-33"
        }
    )

    try:
        with urllib.request.urlopen(request_zip, timeout=30) as respuesta:
            datos_zip = respuesta.read(
                MAX_ZIP_BYTES + 1
            )

    except Exception as error:
        raise ValueError(
            "No se pudo descargar el repositorio desde GitHub."
        ) from error

    if len(datos_zip) > MAX_ZIP_BYTES:
        raise ValueError(
            "El repositorio supera el límite permitido de 50 MB."
        )

    return repositorio, datos_zip
class ArchivoGitHub:
    def __init__(self, nombre, datos):
        self.name = f"{nombre}.zip"
        self._datos = datos

    def getvalue(self):
        return self._datos


def extraer_zip_seguro(datos, destino):
    if len(datos) > MAX_ZIP_BYTES:
        raise ValueError("El ZIP supera el límite permitido de 50 MB.")

    destino = Path(destino).resolve()
    destino.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(io.BytesIO(datos)) as archivo_zip:
        for miembro in archivo_zip.infolist():
            ruta_destino = (destino / miembro.filename).resolve()

            if ruta_destino != destino and destino not in ruta_destino.parents:
                raise ValueError("El ZIP contiene una ruta no válida.")

            # Rechaza enlaces simbólicos para evitar escribir fuera del directorio temporal.
            tipo_unix = (miembro.external_attr >> 16) & 0o170000
            if tipo_unix == 0o120000:
                raise ValueError("El ZIP contiene un enlace simbólico no permitido.")

            if miembro.is_dir():
                ruta_destino.mkdir(parents=True, exist_ok=True)
                continue

            ruta_destino.parent.mkdir(parents=True, exist_ok=True)
            with archivo_zip.open(miembro) as origen, open(ruta_destino, "wb") as salida:
                salida.write(origen.read())

    return destino


def construir_corrida(archivo, resultado):
    return f"""# Corrida de evaluación

- Trabajo: {archivo.name}
- Fecha: {resultado["fecha_evaluacion"]}
- Modelo: {resultado["modelo"]}
- Tokens de entrada: {resultado["input_tokens"]}
- Tokens de salida: {resultado["output_tokens"]}
- Tokens totales: {resultado["total_tokens"]}

## Entrada

{resultado["entrada"]}

## Salida del agente

{resultado["texto"]}
"""


# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================

st.set_page_config(
    page_title="Agente Evaluador - Grupo 33",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# ESTILO VISUAL
# =========================================================

st.markdown(
    """
    <style>

    /* -------------------------------------------------
       CONFIGURACIÓN GENERAL
    ------------------------------------------------- */

    .stApp {
        background-color: #f5f6f8;
    }

    .block-container {
        padding-top: 1.3rem;
        padding-bottom: 3rem;
        max-width: 1450px;
    }

    h1, h2, h3 {
        color: #26364a;
    }


    /* -------------------------------------------------
       CABECERA UCEMA
    ------------------------------------------------- */

    .ucema-header {
        background: linear-gradient(
            135deg,
            #8b0029 0%,
            #a90032 55%,
            #780024 100%
        );

        border-radius: 16px;
        padding: 26px 34px;
        margin-bottom: 24px;

        box-shadow:
            0 7px 18px rgba(0, 0, 0, 0.12);
    }

    .ucema-header h1 {
        color: white !important;
        margin: 0;
        font-size: 2.05rem;
        font-weight: 750;
    }

    .ucema-header h2 {
        color: #f6dce4 !important;
        font-size: 1.05rem;
        margin-top: 6px;
        margin-bottom: 0;
        font-weight: 450;
    }

    .ucema-header p {
        color: #ffffff;
        margin-top: 15px;
        margin-bottom: 0;
        max-width: 850px;
        line-height: 1.5;
    }


    /* -------------------------------------------------
       PASOS
    ------------------------------------------------- */

    .steps {
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 8px 0 30px 0;
        gap: 12px;
    }

    .step {
        background-color: white;
        border: 1px solid #dedfe3;
        border-radius: 30px;
        padding: 10px 22px;
        color: #42526e;
        font-weight: 600;
        font-size: 0.95rem;

        box-shadow:
            0 3px 8px rgba(0,0,0,0.05);
    }

    .step-number {
        background-color: #a90032;
        color: white;
        border-radius: 50%;
        width: 26px;
        height: 26px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        margin-right: 8px;
        font-size: 0.85rem;
    }

    .step-arrow {
        color: #a7a7a7;
        font-size: 1.3rem;
        font-weight: bold;
    }


    /* -------------------------------------------------
       TARJETAS
    ------------------------------------------------- */

    .card {
        background-color: white;
        border-radius: 16px;
        border: 1px solid #e1e4e8;
        padding: 24px 26px;
        margin-bottom: 18px;

        box-shadow:
            0 4px 12px rgba(0, 0, 0, 0.045);
    }

    .card-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #26364a;
        margin-bottom: 10px;
    }

    .card-subtitle {
        color: #6b778c;
        line-height: 1.5;
        margin-bottom: 8px;
    }


    /* -------------------------------------------------
       ÁREA DE CARGA
    ------------------------------------------------- */

    [data-testid="stFileUploader"] {
        background-color: white;
        border-radius: 14px;
        border: 1px solid #dfe2e6;
        padding: 14px;
    }

    [data-testid="stFileUploaderDropzone"] {
        background-color: #fafafa;
        border: 2px dashed #c8cdd4;
        border-radius: 12px;
        padding-top: 28px;
        padding-bottom: 28px;
    }


    /* -------------------------------------------------
       BOTONES
    ------------------------------------------------- */

    div.stButton > button[kind="primary"] {

        background: linear-gradient(
            135deg,
            #a90032,
            #840027
        );

        border: none;
        color: white;

        font-weight: 700;

        min-height: 48px;

        border-radius: 9px;

        box-shadow:
            0 4px 10px rgba(169, 0, 50, 0.20);
    }

    div.stButton > button[kind="primary"]:hover {

        background:
            #780024;

        color: white;

        border: none;
    }

    div.stDownloadButton > button {

        border-radius: 9px;

        min-height: 45px;

        font-weight: 600;
    }


    /* -------------------------------------------------
       PANEL INFORMATIVO DERECHO
    ------------------------------------------------- */

    .info-card {

        background-color: white;

        border-radius: 16px;

        padding: 24px 26px;

        border:
            1px solid #e1e4e8;

        margin-bottom: 18px;

        box-shadow:
            0 4px 12px
            rgba(0,0,0,0.045);
    }

    .info-card h3 {

        color: #26364a;

        margin-top: 0;

        margin-bottom: 16px;
    }

    .info-item {

        margin-bottom: 11px;

        color: #42526e;

        line-height: 1.45;
    }

    .check {

        color: #27864a;

        font-weight: bold;

        margin-right: 8px;
    }


    /* -------------------------------------------------
       RESULTADOS
    ------------------------------------------------- */

    .result-header {

        background-color: white;

        border-radius: 16px;

        padding: 24px 28px;

        margin-top: 15px;

        margin-bottom: 18px;

        border:
            1px solid #e1e4e8;

        border-left:
            6px solid #a90032;

        box-shadow:
            0 4px 12px
            rgba(0,0,0,0.05);
    }

    .result-header h2 {

        margin: 0;

        color: #26364a;
    }

    .result-header p {

        margin-top: 8px;

        margin-bottom: 0;

        color: #6b778c;
    }


    /* -------------------------------------------------
       TARJETAS DE ESTADO
    ------------------------------------------------- */

    .success-card {

        background-color: #eef8f1;

        border:
            1px solid #b9dec4;

        border-left:
            6px solid #2e8b57;

        border-radius: 12px;

        padding: 18px 22px;

        margin-bottom: 14px;
    }

    .warning-card {

        background-color: #fff8e7;

        border:
            1px solid #ecd79d;

        border-left:
            6px solid #d89d20;

        border-radius: 12px;

        padding: 18px 22px;

        margin-bottom: 14px;
    }

    .fraud-card {

        background-color: #faeeee;

        border:
            1px solid #dfb5b5;

        border-left:
            6px solid #9d1f2f;

        border-radius: 12px;

        padding: 18px 22px;

        margin-bottom: 14px;
    }

    .status-title {

        font-weight: 750;

        font-size: 1.02rem;

        margin-bottom: 4px;
    }


    /* -------------------------------------------------
       RESULTADO COMPLETO
    ------------------------------------------------- */

    .evaluation-container {

        background-color: white;

        padding: 28px 32px;

        border-radius: 16px;

        border:
            1px solid #e1e4e8;

        box-shadow:
            0 4px 12px
            rgba(0,0,0,0.045);

        margin-bottom: 18px;
    }


    /* -------------------------------------------------
       SIDEBAR
    ------------------------------------------------- */

    [data-testid="stSidebar"] {

        background-color: #ffffff;

        border-right:
            1px solid #e1e4e8;
    }

    [data-testid="stSidebar"] h2 {

        color: #a90032;
    }

    .sidebar-title {

        font-size: 1.25rem;

        font-weight: 750;

        color: #a90032;

        margin-bottom: 5px;
    }

    .sidebar-subtitle {

        color: #7a869a;

        font-size: 0.87rem;

        margin-bottom: 24px;
    }

    .menu-item {

        background-color: #f7f7f8;

        padding:
            11px 14px;

        margin-bottom:
            8px;

        border-radius:
            9px;

        font-weight:
            550;

        color:
            #344563;
    }

    .menu-active {

        background-color:
            #f7e9ee;

        border-left:
            4px solid #a90032;

        color:
            #850027;
    }


    /* -------------------------------------------------
       PIE
    ------------------------------------------------- */

    .footer {

        text-align:
            center;

        color:
            #8993a4;

        margin-top:
            40px;

        padding-top:
            20px;

        border-top:
            1px solid #e1e4e8;

        font-size:
            0.85rem;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# MENÚ LATERAL
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div class="sidebar-title">
        🎓 Agente Evaluador
        </div>

        <div class="sidebar-subtitle">
        Grupo 33 · MBA UCEMA
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="menu-item menu-active">
        🏠 Inicio
        </div>

        <div class="menu-item">
        📄 Cargar trabajos
        </div>

        <div class="menu-item">
        📊 Resultados
        </div>

        <div class="menu-item">
        👥 Grupo 33
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### 👥 Integrantes")

    st.write("Héctor Gustavo Beretta")
    st.write("Eliana Androszczuk")
    st.write("Diego Gonzalez")
    st.write("Agustin Poselski")

    st.divider()

    st.caption(
        "MBA UCEMA · 2026"
    )


# =========================================================
# CABECERA
# =========================================================

col_header, col_logo = st.columns(
    [5, 1],
    vertical_alignment="center"
)

with col_header:

    st.markdown(
        '<div class="ucema-header">'
        '<h1>AGENTE EVALUADOR - GRUPO 33</h1>'
        '<h2>MBA UCEMA · Creación de Agentes de IA</h2>'
        '<p>Evaluación automática, objetiva y trazable de trabajos académicos mediante una rúbrica ejecutable.</p>'
        '</div>',
        unsafe_allow_html=True
    )

with col_logo:

    st.image(
        "assets/Logo_UCEMA.png",
        use_container_width=True
    )


# =========================================================
# PASOS VISUALES
# =========================================================

st.markdown(
    '<div class="steps">'
    '<div class="step"><span class="step-number">1</span>Cargar trabajo</div>'
    '<div class="step-arrow">→</div>'
    '<div class="step"><span class="step-number">2</span>Evaluar</div>'
    '<div class="step-arrow">→</div>'
    '<div class="step"><span class="step-number">3</span>Resultados</div>'
    '</div>',
    unsafe_allow_html=True
)

# =========================================================
# ÁREA PRINCIPAL
# =========================================================

col_principal, col_info = st.columns(
    [1.8, 1],
    gap="large"
)


# =========================================================
# COLUMNA PRINCIPAL
# =========================================================

with col_principal:

    st.markdown(
        '<div class="card">'
        '<div class="card-title">📄 Cargar trabajo</div>'
        '<div class="card-subtitle">'
        'Subí un ZIP con el repositorio completo, cargá archivos individuales para una prueba rápida o ingresá la URL de un repositorio público de GitHub.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    archivos = st.file_uploader(
        "Arrastrá los archivos aquí o presioná Examinar",
        type=[
            "zip",
            "md",
            "txt",
            "py",
            "json"
        ],
        accept_multiple_files=True
    )
    
    st.markdown(
    "<div style='text-align:center; margin:12px 0; font-weight:600;'>O</div>",
    unsafe_allow_html=True
    )

    urls_github_texto = st.text_area(
        "🔗 Repositorios públicos de GitHub",
        placeholder=(
            "https://github.com/usuario/repositorio1\n"
            "https://github.com/usuario/repositorio2\n"
            "https://github.com/usuario/repositorio3"
        ),
        help="Pegá una URL pública de GitHub por línea."
    )

    urls_github = [
        url.strip()
        for url in urls_github_texto.splitlines()
        if url.strip()
    ]

    if archivos:

        st.success(
            f"✓ {len(archivos)} archivo(s) cargado(s) correctamente."
        )

        for archivo in archivos:

            etiqueta = "repositorio ZIP" if archivo.name.lower().endswith(".zip") else "archivo individual"
            st.write(f"📦 {archivo.name} ({etiqueta})")


    st.markdown("<br>", unsafe_allow_html=True)


    st.markdown(
        '<div class="card">'
        '<div class="card-title">⚙️ Ejecutar evaluación</div>'
        '<div class="card-subtitle">'
        'El agente realizará el control de posibles manipulaciones y posteriormente aplicará la rúbrica académica.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


    boton_evaluar = st.button(
        "▶  Evaluar trabajos",
        type="primary",
        disabled=not archivos and not urls_github,
        use_container_width=True
    )


# =========================================================
# COLUMNA DERECHA
# =========================================================

with col_info:

        st.markdown(
        '<div class="info-card">'
        '<h3>🎯 ¿Qué hace este agente?</h3>'
        '<div class="info-item"><span class="check">✓</span> Aplica una rúbrica ejecutable.</div>'
        '<div class="info-item"><span class="check">✓</span> Evalúa múltiples trabajos.</div>'
        '<div class="info-item"><span class="check">✓</span> Controla posibles intentos de manipulación.</div>'
        '<div class="info-item"><span class="check">✓</span> Genera devoluciones detalladas.</div>'
        '<div class="info-item"><span class="check">✓</span> Identifica oportunidades concretas de mejora.</div>'
        '<div class="info-item"><span class="check">✓</span> Permite descargar cada evaluación.</div>'
        '</div>'
        '<div class="info-card">'
        '<h3>🔎 Evaluación trazable</h3>'
        '<div class="info-item">El agente analiza las evidencias disponibles en el trabajo y fundamenta la evaluación obtenida.</div>'
        '</div>'
        '<div class="info-card">'
        '<h3>ℹ️ Trabajo académico</h3>'
        '<div class="info-item">Aplicación desarrollada por el Grupo 33 como trabajo parcial del MBA UCEMA 2026.</div>'
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# RESULTADOS
# =========================================================

if boton_evaluar:

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        '<div class="result-header">'
        '<h2>📊 Resultados de la evaluación</h2>'
        '<p>A continuación se presenta la devolución generada por el Agente Evaluador.</p>'
        '</div>',
        unsafe_allow_html=True
    )


    trabajos_a_evaluar = list(archivos or [])

    for url_github in urls_github:
        try:
            with st.spinner(
                f"Descargando repositorio desde GitHub: {url_github}"
            ):
                nombre_repo, datos_repo = descargar_repositorio_github(
                    url_github
                )

            trabajos_a_evaluar.append(
                ArchivoGitHub(nombre_repo, datos_repo)
            )

            st.success(
                f"✓ Repositorio GitHub descargado correctamente: {nombre_repo}"
            )

        except ValueError as error:
            st.error(
                f"No se pudo cargar {url_github}: {error}"
            )

    for archivo in trabajos_a_evaluar:

        st.markdown(
            f'<div class="card">'
            f'<div class="card-title">📄 {archivo.name}</div>'
            f'<div class="card-subtitle">Trabajo seleccionado para evaluación.</div>'
            f'</div>',
            unsafe_allow_html=True
        )

        with tempfile.TemporaryDirectory() as directorio_temporal:
            try:
                if archivo.name.lower().endswith(".zip"):
                    ruta_trabajo = extraer_zip_seguro(
                        archivo.getvalue(),
                        Path(directorio_temporal) / "repositorio"
                    )
                    descripcion_trabajo = "repositorio completo"

                else:
                    ruta_trabajo = (
                        Path(directorio_temporal)
                        / Path(archivo.name).name
                    )

                    ruta_trabajo.write_bytes(
                        archivo.getvalue()
                    )

                    descripcion_trabajo = "archivo individual"

                with st.spinner(
                    f"Evaluando {archivo.name} ({descripcion_trabajo})..."
                ):
                    resultado = evaluar_trabajo(
                        ruta_trabajo
                    )

            except (ValueError, zipfile.BadZipFile) as error:
                st.error(
                    f"No se pudo procesar {archivo.name}: {error}"
                )
                continue
        # ============================================================
        # DATOS PARA EL DASHBOARD VISUAL
        # Solo interpreta el texto generado por el evaluador.
        # No modifica la evaluación ni recalcula puntajes.
        # ============================================================

        texto_resultado = resultado["texto"]

        # Extraer nota final
        match_nota = re.search(
            r"NOTA FINAL:\s*(\d+)\s*/\s*100",
            texto_resultado,
            re.IGNORECASE
        )

        nota_final = int(match_nota.group(1)) if match_nota else 0

        # Extraer puntajes de las cinco dimensiones
        dimensiones_dashboard = [
            ("Sistema completo y funcionando", 30),
            ("Proceso documentado", 25),
            ("Formato y reproducibilidad", 15),
            ("Análisis económico", 15),
            ("Gobierno y riesgo", 15),
        ]

        puntajes_dashboard = []

        for nombre_dimension, maximo in dimensiones_dashboard:
            patron = rf"\|\s*{re.escape(nombre_dimension)}\s*\|\s*(\d+)\s*/\s*{maximo}\s*\|"
            coincidencia = re.search(
                patron,
                texto_resultado,
                re.IGNORECASE
            )

            puntaje = int(coincidencia.group(1)) if coincidencia else 0

            puntajes_dashboard.append(
                (nombre_dimension, puntaje, maximo)
            )
            
        st.success(
            f"✓ Evaluación completada: {archivo.name}"
        )

        # ---------------------------------------------
        # TARJETAS VISUALES DE RESULTADO
        # ---------------------------------------------

        col_fortaleza, col_mejora, col_fraude = st.columns(3)

        with col_fortaleza:
            st.markdown(
                '<div class="success-card">'
                '<div class="status-title">✓ Fortalezas</div>'
                'Aspectos correctamente resueltos por el trabajo evaluado.'
                '</div>',
                unsafe_allow_html=True
            )

        with col_mejora:
            st.markdown(
                '<div class="warning-card">'
                '<div class="status-title">⚠ Aspectos a mejorar</div>'
                'Oportunidades de mejora identificadas por el evaluador.'
                '</div>',
                unsafe_allow_html=True
            )

        with col_fraude:
            st.markdown(
                '<div class="fraud-card">'
                '<div class="status-title">🔎 Control de fraude</div>'
                'Verificación de posibles intentos de manipulación del evaluador.'
                '</div>',
                unsafe_allow_html=True
            )

    
        # ---------------------------------------------
        # EVALUACIÓN COMPLETA
        # ---------------------------------------------

        with st.container(
            border=True
        ):

            st.markdown(
                "### 📋 Evaluación completa"
            )

            st.markdown(
                resultado["texto"]
            )


        # ---------------------------------------------
        # BOTONES INFERIORES
        # ---------------------------------------------

        col_descargar, col_nuevo = st.columns(
            [1, 1]
        )


        with col_descargar:

            st.download_button(

                label=
                "⬇ Descargar evaluación",

                data=
                resultado["texto"],

                file_name=
                f"{archivo.name}_evaluacion.md",

                mime=
                "text/markdown",

                key=
                f"descarga_{archivo.name}",

                use_container_width=True
            )

            st.download_button(
                label="⬇ Descargar corrida completa",
                data=construir_corrida(archivo, resultado),
                file_name=f"{archivo.name}_corrida.md",
                mime="text/markdown",
                key=f"corrida_{archivo.name}",
                use_container_width=True
            )


        with col_nuevo:

            if st.button(
                "↻ Evaluar otro trabajo",
                key=f"nuevo_{archivo.name}",
                use_container_width=True
            ):

                st.rerun()


        st.markdown("<br>", unsafe_allow_html=True)


# =========================================================
# PIE
# =========================================================

st.markdown(
    """
    <div class="footer">

    Agente Evaluador · Grupo 33 ·
    MBA UCEMA · 2026

    </div>
    """,
    unsafe_allow_html=True
)
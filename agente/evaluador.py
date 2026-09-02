import os
from datetime import datetime
from zoneinfo import ZoneInfo
from pathlib import Path
from openai import OpenAI


# ---------------------------------------------------------
# CONFIGURACIÓN
# ---------------------------------------------------------

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

BASE_DIR = Path(__file__).resolve().parent
REPO_DIR = BASE_DIR.parent


# ---------------------------------------------------------
# FUNCIÓN PARA LEER ARCHIVOS
# ---------------------------------------------------------

def leer_archivo(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        return archivo.read()


# ---------------------------------------------------------
# CARGAR INSTRUCCIONES DEL AGENTE
# ---------------------------------------------------------

system_prompt = leer_archivo(BASE_DIR / "system_prompt.md")
rubrica = leer_archivo(REPO_DIR / "rubrica.md")
formato_salida = leer_archivo(REPO_DIR / "formato_salida.md")


# ---------------------------------------------------------
# FUNCIÓN PRINCIPAL DEL AGENTE EVALUADOR
# ---------------------------------------------------------

def evaluar_trabajo(ruta_trabajo):

    trabajo = leer_archivo(ruta_trabajo)
    fecha_evaluacion = datetime.now(ZoneInfo("America/Santiago")).strftime("%d/%m/%Y")

    instrucciones = f"""
{system_prompt}

RÚBRICA DE EVALUACIÓN:
{rubrica}

FORMATO DE SALIDA:
{formato_salida}
"""

    entrada = f"""
Evaluá el siguiente trabajo aplicando estrictamente
la rúbrica y el formato de salida indicados.

La fecha de evaluación es: {fecha_evaluacion}.
Debes utilizar exactamente esta fecha en la respuesta.

TRABAJO A EVALUAR:

{trabajo}
"""

    respuesta = client.responses.create(
        model="gpt-5.6",
        instructions=instrucciones,
        input=entrada
    )

    return respuesta.output_text


# ---------------------------------------------------------
# EJECUCIÓN DE PRUEBA
# ---------------------------------------------------------

if __name__ == "__main__":

    trabajo_prueba = REPO_DIR / "casos" / "intermedio" / "trabajo.md"

    resultado = evaluar_trabajo(trabajo_prueba)

    print("\n--- RESULTADO DE LA EVALUACIÓN ---\n")
    print(resultado)

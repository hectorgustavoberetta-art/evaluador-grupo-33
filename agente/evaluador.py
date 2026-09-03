import os
import re
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

def leer_entrega(ruta):
    ruta = Path(ruta)

    if ruta.is_file():
        return leer_archivo(ruta)

    extensiones_validas = {".md", ".txt", ".py", ".json"}

    partes = []

    for archivo in sorted(ruta.rglob("*")):
        if archivo.is_file() and archivo.suffix.lower() in extensiones_validas:
            contenido = leer_archivo(archivo)

            partes.append(
                f"\n\n===== ARCHIVO: {archivo.relative_to(ruta)} =====\n\n"
                f"{contenido}"
            )

    return "".join(partes)
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

    trabajo = leer_entrega(ruta_trabajo)
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

    casos = ["deficiente", "intermedio", "excelente"]
    repeticiones = 3

    resultados_dir = REPO_DIR / "resultados"
    resultados_dir.mkdir(exist_ok=True)

    for caso in casos:

        print(f"\n{'=' * 60}")
        print(f"EVALUANDO CASO: {caso.upper()}")
        print(f"{'=' * 60}\n")

        ruta_caso = REPO_DIR / "casos" / caso / "trabajo.md"

        resultados = []
        puntajes = []

        for numero in range(1, repeticiones + 1):

            print(f"\n--- Ejecución {numero} de {repeticiones} ---\n")

            resultado = evaluar_trabajo(ruta_caso)
            resultados.append(resultado)

            coincidencia = re.search(
                r"Puntaje total.*?(\d+)\s*/\s*100",
                resultado,
                re.IGNORECASE
            )

            if coincidencia:
                puntaje = int(coincidencia.group(1))
                puntajes.append(puntaje)
                print(f"Puntaje obtenido: {puntaje}/100")
            else:
                print("No se pudo identificar el puntaje.")

        if puntajes:
            promedio = sum(puntajes) / len(puntajes)

            print(f"\nPuntajes obtenidos: {puntajes}")
            print(f"PROMEDIO: {promedio:.2f}/100")

            archivo_salida = resultados_dir / f"{caso}.md"

            with open(archivo_salida, "w", encoding="utf-8") as archivo:
                archivo.write(f"# Calibración del caso {caso}\n\n")
                archivo.write(f"Puntajes obtenidos: {puntajes}\n\n")
                archivo.write(f"Promedio: {promedio:.2f}/100\n\n")

                for numero, resultado in enumerate(resultados, start=1):
                    archivo.write(
                        f"\n\n# Ejecución {numero}\n\n{resultado}\n"
                    )

            print(f"\nResultado guardado en: {archivo_salida}")
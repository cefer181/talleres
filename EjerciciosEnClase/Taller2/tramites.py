"""
tramites.py — Módulo base para el Taller Práctico N.º 2

Curso: GitHub Copilot para Desarrollo y Aseguramiento de la Calidad
CEC-EPN — Unidad de Capacitación y Certificación
Instructor: Ing. Danny Esteban Venegas Villavicencio

CONTEXTO
--------
Este módulo simula el procesamiento del registro diario de trámites de una
ventanilla de atención. Contiene funciones de validación y de cálculo que
actualmente NO tienen pruebas automatizadas.

Su tarea en el Taller N.º 2 consiste en construir esa batería de pruebas con
pytest, apoyándose en GitHub Copilot (plan Free), ejecutarla, interpretar los
resultados y corregir los errores que las pruebas revelen.

IMPORTANTE
----------
* El módulo funciona en apariencia: ejecutarlo no produce ningún fallo visible.
  Los defectos aparecen únicamente cuando se prueban los casos límite y los
  casos de error.
* No modifique las firmas de las funciones (nombres y parámetros): sus pruebas
  deben escribirse sobre esta interfaz.
* Los datos son ficticios. No incorpore información institucional real.

Requisitos: Python 3.12 y pytest (pip install pytest). Sin dependencias externas.
"""

from datetime import date

# Umbrales de clasificación del tiempo de atención, en minutos.
LIMITE_AGIL = 10
LIMITE_NORMAL = 30

DIAS_POR_MES = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def validar_cedula(cedula):
    """Valida que una cédula tenga exactamente 10 dígitos numéricos.

    Parámetros:
        cedula (str): número de cédula a validar.

    Retorna:
        bool: True si la cédula es válida, False en caso contrario.
    """
    if cedula is None:
        return False
    cedula = str(cedula).strip()
    if len(cedula) != 10:
        return False
    return cedula.isdigit()


def validar_fecha(texto):
    """Valida una fecha en formato dd/mm/aaaa y verifica que exista.

    Parámetros:
        texto (str): fecha en formato dd/mm/aaaa, por ejemplo "03/08/2026".

    Retorna:
        bool: True si la fecha es válida, False en caso contrario.
    """
    if not isinstance(texto, str):
        return False
    partes = texto.split("/")
    if len(partes) != 3:
        return False
    if not all(p.isdigit() for p in partes):
        return False

    dia, mes, anio = int(partes[0]), int(partes[1]), int(partes[2])
    if mes < 1 or mes > 12:
        return False
    if anio < 1900 or anio > 2100:
        return False
    if dia < 1 or dia > DIAS_POR_MES[mes]:
        return False
    return True


def clasificar_tiempo(minutos):
    """Clasifica un tiempo de atención según su duración.

    Categorías:
        "Ágil"     : hasta 10 minutos, inclusive.
        "Normal"   : de 11 a 30 minutos, inclusive.
        "Demorada" : más de 30 minutos.

    Parámetros:
        minutos (int): tiempo de atención en minutos. Debe ser positivo.

    Retorna:
        str: la categoría correspondiente.

    Lanza:
        ValueError: si el tiempo es negativo.
    """
    if minutos < 0:
        raise ValueError("El tiempo de atención no puede ser negativo.")
    if minutos <= LIMITE_AGIL:
        return "Ágil"
    if minutos <= LIMITE_NORMAL:
        return "Normal"
    return "Demorada"


def calcular_promedio(tiempos):
    """Calcula el tiempo promedio de atención, redondeado a dos decimales.

    Parámetros:
        tiempos (list[int]): lista de tiempos de atención en minutos.

    Retorna:
        float: el promedio de la lista. Para una lista vacía retorna 0.0.
    """
   
    if not tiempos:
        return 0.0

    total = 0

    for t in tiempos:
        total += t

    return round(total / len(tiempos), 2)






def resumen_diario(registros):
    """Consolida el registro diario de trámites atendidos.

    Parámetros:
        registros (list[dict]): cada registro tiene las claves
            "cedula" (str), "fecha" (str, dd/mm/aaaa) y "minutos" (int).

    Retorna:
        dict con las claves:
            "total"          : número de registros válidos procesados.
            "descartados"    : número de registros rechazados por datos inválidos.
            "promedio"       : tiempo promedio de atención de los registros válidos.
            "por_categoria"  : conteo de trámites por categoría de duración.
    """
    validos = []
    descartados = 0

    for r in registros:
        if not validar_cedula(r.get("cedula")):
            descartados += 1
            continue
        if not validar_fecha(r.get("fecha")):
            descartados += 1
            continue
        validos.append(r)

    conteo = {"Ágil": 0, "Normal": 0, "Demorada": 0}
    for r in validos:
        categoria = clasificar_tiempo(r["minutos"])
        conteo[categoria] += 1

    return {
        "total": len(validos),
        "descartados": descartados,
        "promedio": calcular_promedio([r["minutos"] for r in validos]),
        "por_categoria": conteo,
    }


# Datos ficticios de ejemplo para una ejecución rápida del módulo.
REGISTROS_EJEMPLO = [
    {"cedula": "1712345678", "fecha": "03/08/2026", "minutos": 8},
    {"cedula": "1798765432", "fecha": "03/08/2026", "minutos": 25},
    {"cedula": "0923456781", "fecha": "03/08/2026", "minutos": 45},
    {"cedula": "17123",      "fecha": "03/08/2026", "minutos": 12},
    {"cedula": "1755566677", "fecha": "31/02/2026", "minutos": 15},
]


if __name__ == "__main__":
    print(f"Registro de trámites — {date.today().strftime('%d/%m/%Y')}")
    resultado = resumen_diario(REGISTROS_EJEMPLO)
    for clave, valor in resultado.items():
        print(f"  {clave}: {valor}")

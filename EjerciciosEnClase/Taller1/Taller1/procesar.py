import csv
from pathlib import Path

from tramites import validar_cedula, validar_fecha, clasificar_tiempo


def procesar_carpeta(carpeta: str = "datos") -> dict:
    """
    Procesa todos los archivos CSV ubicados en la carpeta de datos.

    Valida:
    - Cédula.
    - Fecha.
    - Minutos de atención.

    Retorna:
    - Total de registros válidos.
    - Total de registros descartados.
    - Promedio de minutos.
    """

    # ============================================================
    # LOCALIZAR AUTOMÁTICAMENTE LA CARPETA DATOS
    # ============================================================

    ruta_script = Path(__file__).resolve().parent

    # Primero busca datos al mismo nivel de procesar.py
    carpeta_path = ruta_script / carpeta

    # Si no existe, busca un nivel arriba
    if not carpeta_path.exists():
        carpeta_path = ruta_script.parent / carpeta

    carpeta_path = carpeta_path.resolve()

    print()
    print("=" * 80)
    print("              SISTEMA DE PROCESAMIENTO DE TRÁMITES")
    print("=" * 80)
    print(f"Carpeta de datos: {carpeta_path}")
    print("=" * 80)

    # ============================================================
    # VALIDAR CARPETA
    # ============================================================

    if not carpeta_path.exists():
        raise FileNotFoundError(
            f"No existe la carpeta de datos: {carpeta_path}"
        )

    if not carpeta_path.is_dir():
        raise NotADirectoryError(
            f"La ruta indicada no es una carpeta: {carpeta_path}"
        )

    # ============================================================
    # BUSCAR ARCHIVOS CSV
    # ============================================================

    archivos_csv = sorted(carpeta_path.glob("*.csv"))

    if not archivos_csv:
        print()
        print("[ADVERTENCIA] No se encontraron archivos CSV.")
        print()

        return {
            "archivos_procesados": 0,
            "total_validas": 0,
            "total_descartadas": 0,
            "promedio_minutos": 0.0
        }

    # ============================================================
    # CONTADORES GENERALES
    # ============================================================

    total_archivos = 0
    total_validas = 0
    total_descartadas = 0
    suma_minutos = 0

    # ============================================================
    # RECORRER ARCHIVOS
    # ============================================================

    for archivo_csv in archivos_csv:

        if not archivo_csv.is_file():
            continue

        total_archivos += 1

        validas_archivo = 0
        descartadas_archivo = 0

        print()
        print("-" * 80)
        print(f"ARCHIVO #{total_archivos}: {archivo_csv.name}")
        print("-" * 80)

        try:
            # utf-8-sig permite manejar archivos con BOM
            with archivo_csv.open(
                "r",
                encoding="utf-8-sig",
                newline=""
            ) as archivo:

                lector = csv.DictReader(archivo)

                # ====================================================
                # VALIDAR CABECERAS
                # ====================================================

                columnas_requeridas = {
                    "cedula",
                    "fecha",
                    "minutos"
                }

                columnas_encontradas = set(
                    lector.fieldnames or []
                )

                faltantes = (
                    columnas_requeridas -
                    columnas_encontradas
                )

                if faltantes:
                    print(
                        "[ERROR] El archivo no contiene "
                        "las columnas requeridas."
                    )

                    print(
                        "Columnas faltantes:",
                        ", ".join(sorted(faltantes))
                    )

                    continue

                # ====================================================
                # PROCESAR FILAS
                # ====================================================

                for numero_fila, fila in enumerate(
                    lector,
                    start=2
                ):

                    cedula = (
                        fila.get("cedula", "") or ""
                    ).strip()

                    fecha = (
                        fila.get("fecha", "") or ""
                    ).strip()

                    minutos_texto = (
                        fila.get("minutos", "") or ""
                    ).strip()

                    # --------------------------------------------
                    # VALIDAR MINUTOS
                    # --------------------------------------------

                    try:
                        minutos = int(minutos_texto)

                    except (TypeError, ValueError):

                        total_descartadas += 1
                        descartadas_archivo += 1

                        print(
                            f"[DESCARTADO] Fila {numero_fila} | "
                            f"Minutos inválidos: "
                            f"'{minutos_texto}'"
                        )

                        continue

                    # --------------------------------------------
                    # VALIDAR CÉDULA
                    # --------------------------------------------

                    if not validar_cedula(cedula):

                        total_descartadas += 1
                        descartadas_archivo += 1

                        print(
                            f"[DESCARTADO] Fila {numero_fila} | "
                            f"Cédula inválida: '{cedula}'"
                        )

                        continue

                    # --------------------------------------------
                    # VALIDAR FECHA
                    # --------------------------------------------

                    if not validar_fecha(fecha):

                        total_descartadas += 1
                        descartadas_archivo += 1

                        print(
                            f"[DESCARTADO] Fila {numero_fila} | "
                            f"Fecha inválida: '{fecha}'"
                        )

                        continue

                    # --------------------------------------------
                    # CLASIFICAR TIEMPO
                    # --------------------------------------------

                    try:
                        clasificacion = clasificar_tiempo(
                            minutos
                        )

                    except ValueError as error:

                        total_descartadas += 1
                        descartadas_archivo += 1

                        print(
                            f"[DESCARTADO] Fila {numero_fila} | "
                            f"Minutos: {minutos} | "
                            f"Motivo: {error}"
                        )

                        continue

                    # --------------------------------------------
                    # REGISTRO VÁLIDO
                    # --------------------------------------------

                    total_validas += 1
                    validas_archivo += 1
                    suma_minutos += minutos

                    print(
                        f"[VÁLIDO]     Fila {numero_fila} | "
                        f"Cédula: {cedula} | "
                        f"Fecha: {fecha} | "
                        f"Minutos: {minutos} | "
                        f"Clasificación: {clasificacion}"
                    )

        except UnicodeDecodeError:
            print(
                f"[ERROR] No se pudo leer "
                f"{archivo_csv.name}. "
                f"Verifique la codificación del archivo."
            )

        except Exception as error:
            print(
                f"[ERROR] Problema procesando "
                f"{archivo_csv.name}: {error}"
            )

        # ========================================================
        # RESUMEN POR ARCHIVO
        # ========================================================

        print()
        print(f"Resumen de {archivo_csv.name}")
        print(f"  Registros válidos       : {validas_archivo}")
        print(f"  Registros descartados   : {descartadas_archivo}")

    # ============================================================
    # CALCULAR PROMEDIO
    # ============================================================

    if total_validas > 0:
        promedio = round(
            suma_minutos / total_validas,
            2
        )
    else:
        promedio = 0.0

    # ============================================================
    # RESULTADO
    # ============================================================

    resultado = {
        "archivos_procesados": total_archivos,
        "total_validas": total_validas,
        "total_descartadas": total_descartadas,
        "promedio_minutos": promedio
    }

    # ============================================================
    # MOSTRAR RESUMEN GENERAL EN CONSOLA
    # ============================================================

    print()
    print("=" * 80)
    print("                     RESULTADO GENERAL")
    print("=" * 80)
    print(
        f"Archivos procesados       : "
        f"{resultado['archivos_procesados']}"
    )
    print(
        f"Registros válidos         : "
        f"{resultado['total_validas']}"
    )
    print(
        f"Registros descartados     : "
        f"{resultado['total_descartadas']}"
    )
    print(
        f"Promedio de minutos       : "
        f"{resultado['promedio_minutos']}"
    )
    print("=" * 80)
    print("PROCESAMIENTO FINALIZADO CORRECTAMENTE")
    print("=" * 80)

    return resultado


# ================================================================
# EJECUCIÓN PRINCIPAL
# ================================================================

if __name__ == "__main__":

    try:

        procesar_carpeta("datos")

    except FileNotFoundError as error:

        print()
        print("=" * 80)
        print("[ERROR] NO SE ENCONTRÓ LA CARPETA DE DATOS")
        print("=" * 80)
        print(error)

    except Exception as error:

        print()
        print("=" * 80)
        print("[ERROR] OCURRIÓ UN PROBLEMA")
        print("=" * 80)
        print(error)    
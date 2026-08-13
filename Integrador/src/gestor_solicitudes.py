"""
Gestor de Solicitudes Ficticias de Atención.

Componente académico para validar, clasificar y procesar
solicitudes utilizando exclusivamente datos ficticios.

Caso Integrador Final

Integrantes:
- César Jácome
- Ximena Angulo
"""

import json
import math
import re
from datetime import datetime
from pathlib import Path
from typing import Any


# ============================================================
# CONSTANTES DE VALIDACIÓN
# ============================================================

PRIORIDADES_VALIDAS = {
    "BAJA",
    "MEDIA",
    "ALTA",
    "CRITICA",
}


ESTADOS_VALIDOS = {
    "REGISTRADA",
    "EN_PROCESO",
    "ATENDIDA",
    "CANCELADA",
}


TIPOS_SOLICITUD_VALIDOS = {
    "CONSULTA",
    "SOLICITUD",
    "RECLAMO",
    "INCIDENCIA",
    "OTRO",
}


FORMATO_FECHA = "%Y-%m-%d"

MIN_SOLICITANTE_LONGITUD = 3
MAX_SOLICITANTE_LONGITUD = 100

MIN_MINUTOS_ATENCION = 0
MAX_MINUTOS_ATENCION = 10080  # 7 días


# SLA ficticio expresado en minutos.
SLA_POR_PRIORIDAD = {
    "CRITICA": 60,
    "ALTA": 240,
    "MEDIA": 1440,
    "BAJA": 2880,
}


CAMPOS_OBLIGATORIOS = {
    "id_solicitud",
    "solicitante",
    "fecha",
    "tipo",
    "prioridad",
    "estado",
    "minutos_atencion",
}


# ============================================================
# EXCEPCIONES
# ============================================================

class ErrorProcesamientoSolicitudes(Exception):
    """
    Error relacionado con el procesamiento de solicitudes.
    """


# ============================================================
# FUNCIONES AUXILIARES PRIVADAS
# ============================================================

def _es_vacio_o_nulo(valor: Any) -> bool:
    """
    Determina si un valor se considera vacío.

    Args:
        valor: Valor que será evaluado.

    Returns:
        True cuando el valor es None, una cadena vacía
        o contiene únicamente espacios.
    """

    if valor is None:
        return True

    if isinstance(valor, str):
        return not valor.strip()

    return False


def _es_numero_valido(valor: Any) -> bool:
    """
    Verifica que un valor sea numérico y finito.

    Se rechazan:
    - bool
    - NaN
    - infinito positivo
    - infinito negativo

    Args:
        valor: Valor a verificar.

    Returns:
        True si corresponde a un int o float válido.
    """

    # bool es subclase de int en Python.
    if isinstance(valor, bool):
        return False

    if not isinstance(valor, (int, float)):
        return False

    # NaN e infinitos se detectan de forma explícita
    # con math.isfinite, evitando la comparación
    # 'valor != valor' que SonarQube reporta.
    if not math.isfinite(valor):
        return False

    return True


# ============================================================
# VALIDACIONES INDIVIDUALES
# ============================================================

def validar_campo_obligatorio(
    valor: Any,
    nombre_campo: str,
) -> tuple[bool, str]:
    """
    Valida que un campo obligatorio contenga información.

    Args:
        valor: Valor a validar.
        nombre_campo: Nombre del campo.

    Returns:
        Tupla:
        (True, "") si es correcto.
        (False, mensaje) si está vacío.
    """

    if _es_vacio_o_nulo(valor):
        return (
            False,
            f"{nombre_campo} es obligatorio y "
            "no puede estar vacío",
        )

    return True, ""


def validar_id_solicitud(
    id_solicitud: Any,
) -> tuple[bool, str]:
    """
    Valida el identificador ficticio de una solicitud.

    Formato requerido:

        SOL-YYYYMMDD-NNN

    Ejemplo:

        SOL-20260812-001

    Args:
        id_solicitud: Identificador a validar.

    Returns:
        Tupla con estado de validación y mensaje.
    """

    valido, mensaje = validar_campo_obligatorio(
        id_solicitud,
        "id_solicitud",
    )

    if not valido:
        return False, mensaje

    if not isinstance(id_solicitud, str):
        return (
            False,
            "id_solicitud debe ser de tipo string",
        )

    patron = r"^SOL-\d{8}-\d{3}$"

    if not re.fullmatch(
        patron,
        id_solicitud,
    ):
        return (
            False,
            "id_solicitud no cumple el formato "
            "SOL-YYYYMMDD-NNN",
        )

    # Validar que los ocho dígitos del ID
    # correspondan a una fecha existente.
    fecha_id = id_solicitud[4:12]

    try:
        datetime.strptime(
            fecha_id,
            "%Y%m%d",
        )

    except ValueError:
        return (
            False,
            "id_solicitud contiene una fecha inexistente",
        )

    return True, ""


def validar_solicitante(
    solicitante: Any,
) -> tuple[bool, str]:
    """
    Valida el nombre ficticio del solicitante.

    Args:
        solicitante: Nombre a validar.

    Returns:
        Tupla con estado y mensaje de validación.
    """

    valido, mensaje = validar_campo_obligatorio(
        solicitante,
        "solicitante",
    )

    if not valido:
        return False, mensaje

    if not isinstance(
        solicitante,
        str,
    ):
        return (
            False,
            "solicitante debe ser de tipo string",
        )

    solicitante = solicitante.strip()

    if (
        len(solicitante)
        < MIN_SOLICITANTE_LONGITUD
    ):
        return (
            False,
            "solicitante debe contener al menos "
            f"{MIN_SOLICITANTE_LONGITUD} caracteres",
        )

    if (
        len(solicitante)
        > MAX_SOLICITANTE_LONGITUD
    ):
        return (
            False,
            "solicitante no puede superar "
            f"{MAX_SOLICITANTE_LONGITUD} caracteres",
        )

    patron = (
        r"^[A-Za-zÁÉÍÓÚáéíóúÑñ]"
        r"[A-Za-zÁÉÍÓÚáéíóúÑñ0-9\s\-]*$"
    )

    if not re.fullmatch(
        patron,
        solicitante,
    ):
        return (
            False,
            "solicitante contiene caracteres "
            "no permitidos",
        )

    return True, ""


def validar_fecha(
    fecha: Any,
    nombre_campo: str = "fecha",
) -> tuple[bool, str]:
    """
    Valida una fecha utilizando estrictamente
    el formato YYYY-MM-DD.

    Ejemplo válido:

        2026-08-12

    Ejemplos inválidos:

        2026-8-12
        2026-08-2
        12/08/2026
        2026-02-30

    Args:
        fecha: Fecha que será validada.
        nombre_campo: Nombre del campo.

    Returns:
        Tupla con estado y mensaje de validación.
    """

    valido, mensaje = validar_campo_obligatorio(
        fecha,
        nombre_campo,
    )

    if not valido:
        return False, mensaje

    if not isinstance(
        fecha,
        str,
    ):
        return (
            False,
            f"{nombre_campo} debe ser de tipo string",
        )

    # --------------------------------------------------------
    # CORRECCIÓN IDENTIFICADA MEDIANTE PYTEST
    # --------------------------------------------------------
    #
    # datetime.strptime acepta valores como:
    #
    # 2026-8-12
    #
    # aunque la especificación exige:
    #
    # YYYY-MM-DD
    #
    # Por ello se comprueba primero el formato mediante
    # expresión regular.
    # --------------------------------------------------------

    patron_fecha = r"^\d{4}-\d{2}-\d{2}$"

    if not re.fullmatch(
        patron_fecha,
        fecha,
    ):
        return (
            False,
            f"{nombre_campo} debe tener "
            "formato YYYY-MM-DD",
        )

    try:
        fecha_obj = datetime.strptime(
            fecha,
            FORMATO_FECHA,
        )

    except ValueError:
        return (
            False,
            f"{nombre_campo} debe corresponder "
            "a una fecha existente",
        )

    if fecha_obj.year < 1950:
        return (
            False,
            f"{nombre_campo} no puede ser "
            "anterior a 1950",
        )

    if fecha_obj.year > 2100:
        return (
            False,
            f"{nombre_campo} no puede ser "
            "posterior a 2100",
        )

    return True, ""


def validar_tipo_solicitud(
    tipo: Any,
) -> tuple[bool, str]:
    """
    Verifica que el tipo de solicitud
    corresponda a un valor permitido.
    """

    valido, mensaje = validar_campo_obligatorio(
        tipo,
        "tipo",
    )

    if not valido:
        return False, mensaje

    if not isinstance(
        tipo,
        str,
    ):
        return (
            False,
            "tipo debe ser de tipo string",
        )

    if tipo not in TIPOS_SOLICITUD_VALIDOS:

        valores = ", ".join(
            sorted(
                TIPOS_SOLICITUD_VALIDOS
            )
        )

        return (
            False,
            "tipo no válido. "
            f"Valores permitidos: {valores}",
        )

    return True, ""


def validar_prioridad(
    prioridad: Any,
) -> tuple[bool, str]:
    """
    Verifica que la prioridad esté permitida.
    """

    valido, mensaje = validar_campo_obligatorio(
        prioridad,
        "prioridad",
    )

    if not valido:
        return False, mensaje

    if not isinstance(
        prioridad,
        str,
    ):
        return (
            False,
            "prioridad debe ser de tipo string",
        )

    if prioridad not in PRIORIDADES_VALIDAS:

        valores = ", ".join(
            sorted(
                PRIORIDADES_VALIDAS
            )
        )

        return (
            False,
            "prioridad no válida. "
            f"Valores permitidos: {valores}",
        )

    return True, ""


def validar_estado(
    estado: Any,
) -> tuple[bool, str]:
    """
    Verifica que el estado corresponda
    al flujo permitido.
    """

    valido, mensaje = validar_campo_obligatorio(
        estado,
        "estado",
    )

    if not valido:
        return False, mensaje

    if not isinstance(
        estado,
        str,
    ):
        return (
            False,
            "estado debe ser de tipo string",
        )

    if estado not in ESTADOS_VALIDOS:

        valores = ", ".join(
            sorted(
                ESTADOS_VALIDOS
            )
        )

        return (
            False,
            "estado no válido. "
            f"Valores permitidos: {valores}",
        )

    return True, ""


def validar_minutos_atencion(
    minutos: Any,
) -> tuple[bool, str]:
    """
    Valida el tiempo ficticio de atención.

    El valor debe encontrarse entre:

        0 y 10080 minutos
    """

    if minutos is None:
        return (
            False,
            "minutos_atencion es obligatorio",
        )

    if not _es_numero_valido(
        minutos
    ):
        return (
            False,
            "minutos_atencion debe ser numérico",
        )

    if (
        minutos
        < MIN_MINUTOS_ATENCION
    ):
        return (
            False,
            "minutos_atencion no puede ser negativo",
        )

    if (
        minutos
        > MAX_MINUTOS_ATENCION
    ):
        return (
            False,
            "minutos_atencion excede el máximo "
            f"permitido de "
            f"{MAX_MINUTOS_ATENCION} minutos",
        )

    return True, ""


# ============================================================
# VALIDACIONES DE COHERENCIA
# ============================================================

def validar_coherencia_id_fecha(
    id_solicitud: str,
    fecha: str,
) -> tuple[bool, str]:
    """
    Verifica que la fecha codificada
    en el identificador coincida
    con el campo fecha.

    Ejemplo:

        SOL-20260812-001
        2026-08-12
    """

    valido_id, _ = validar_id_solicitud(
        id_solicitud
    )

    if not valido_id:
        return (
            False,
            "No se puede validar coherencia: "
            "id_solicitud inválido",
        )

    valida_fecha, _ = validar_fecha(
        fecha
    )

    if not valida_fecha:
        return (
            False,
            "No se puede validar coherencia: "
            "fecha inválida",
        )

    fecha_id_str = (
        id_solicitud[4:12]
    )

    fecha_id = datetime.strptime(
        fecha_id_str,
        "%Y%m%d",
    ).strftime(
        FORMATO_FECHA
    )

    if fecha_id != fecha:
        return (
            False,
            "La fecha incluida en id_solicitud "
            f"({fecha_id}) no coincide con "
            f"fecha ({fecha})",
        )

    return True, ""


def validar_coherencia_estado_tiempo(
    estado: str,
    minutos_atencion: int | float,
) -> tuple[bool, str]:
    """
    Comprueba una regla básica de coherencia
    entre el estado y el tiempo de atención.

    Una solicitud REGISTRADA todavía no debe
    disponer de tiempo de atención acumulado.
    """

    if (
        estado == "REGISTRADA"
        and minutos_atencion > 0
    ):
        return (
            False,
            "Una solicitud REGISTRADA no debe "
            "tener tiempo de atención acumulado",
        )

    return True, ""


# ============================================================
# VALIDACIÓN COMPLETA DE SOLICITUD
# ============================================================

def validar_solicitud(
    solicitud: Any,
) -> tuple[bool, list[str]]:
    """
    Valida integralmente una solicitud ficticia.

    Ejecuta todas las reglas posibles y devuelve
    la lista de errores encontrados.

    Args:
        solicitud: Diccionario con la solicitud.

    Returns:
        Tupla:
        (True, []) cuando la solicitud es correcta.
        (False, errores) cuando presenta problemas.
    """

    if not isinstance(
        solicitud,
        dict,
    ):
        return (
            False,
            [
                "La solicitud debe ser "
                "un diccionario"
            ],
        )

    errores: list[str] = []

    # --------------------------------------------------------
    # Campos obligatorios
    # --------------------------------------------------------

    campos_faltantes = [
        campo
        for campo in CAMPOS_OBLIGATORIOS
        if campo not in solicitud
    ]

    if campos_faltantes:

        for campo in sorted(
            campos_faltantes
        ):
            errores.append(
                f"Campo obligatorio ausente: {campo}"
            )

        return False, errores

    # --------------------------------------------------------
    # Validadores individuales
    # --------------------------------------------------------

    validaciones = [
        validar_id_solicitud(
            solicitud["id_solicitud"]
        ),
        validar_solicitante(
            solicitud["solicitante"]
        ),
        validar_fecha(
            solicitud["fecha"]
        ),
        validar_tipo_solicitud(
            solicitud["tipo"]
        ),
        validar_prioridad(
            solicitud["prioridad"]
        ),
        validar_estado(
            solicitud["estado"]
        ),
        validar_minutos_atencion(
            solicitud["minutos_atencion"]
        ),
    ]

    for valido, mensaje in validaciones:

        if not valido:
            errores.append(
                mensaje
            )

    # --------------------------------------------------------
    # Coherencia ID / fecha
    # --------------------------------------------------------

    if not errores:

        coherente, mensaje = (
            validar_coherencia_id_fecha(
                solicitud[
                    "id_solicitud"
                ],
                solicitud[
                    "fecha"
                ],
            )
        )

        if not coherente:
            errores.append(
                mensaje
            )

    # --------------------------------------------------------
    # Coherencia estado / tiempo
    # --------------------------------------------------------

    if not errores:

        coherente, mensaje = (
            validar_coherencia_estado_tiempo(
                solicitud[
                    "estado"
                ],
                solicitud[
                    "minutos_atencion"
                ],
            )
        )

        if not coherente:
            errores.append(
                mensaje
            )

    return (
        len(errores) == 0,
        errores,
    )


# ============================================================
# ESTRUCTURA DEL RESUMEN
# ============================================================

def obtener_resumen_vacio() -> dict[str, Any]:
    """
    Retorna la estructura estándar
    para un resumen vacío.
    """

    return {

        "resumen_general": {

            "total_solicitudes_recibidas": 0,

            "total_solicitudes_validas": 0,

            "total_solicitudes_descartadas": 0,

            "tasa_aceptacion_porcentaje": 0.0,

            "tasa_rechazo_porcentaje": 0.0,
        },

        "metricas_tiempo": {

            "promedio_minutos_atencion": 0.0,

            "minutos_atencion_minimo": None,

            "minutos_atencion_maximo": None,

            "minutos_atencion_total": 0.0,
        },

        "distribucion_prioridad": dict.fromkeys(
            sorted(PRIORIDADES_VALIDAS),
            0,
        ),

        "distribucion_estado": dict.fromkeys(
            sorted(ESTADOS_VALIDOS),
            0,
        ),

        "distribucion_tipo": dict.fromkeys(
            sorted(TIPOS_SOLICITUD_VALIDOS),
            0,
        ),

        "solicitudes_validas": [],

        "solicitudes_descartadas": [],

        "alertas_sla": [],
    }


# ============================================================
# PROCESAMIENTO DE SOLICITUDES
# ============================================================

def procesar_solicitudes(
    solicitudes: list[dict[str, Any]] | None,
) -> dict[str, Any]:
    """
    Procesa una colección completa de solicitudes.

    Las solicitudes inválidas son descartadas sin
    detener el procesamiento de las demás.

    Args:
        solicitudes:
            Lista de solicitudes o None.

    Returns:
        Diccionario con métricas y resultados.

    Raises:
        ErrorProcesamientoSolicitudes:
            Cuando la entrada no es una lista o None.
    """

    if solicitudes is None:
        solicitudes = []

    if not isinstance(
        solicitudes,
        list,
    ):
        raise ErrorProcesamientoSolicitudes(
            "solicitudes debe ser una lista o None"
        )

    resumen = obtener_resumen_vacio()

    resumen[
        "resumen_general"
    ][
        "total_solicitudes_recibidas"
    ] = len(
        solicitudes
    )

    minutos_validos: list[float] = []

    # --------------------------------------------------------
    # Procesar cada solicitud
    # --------------------------------------------------------

    for indice, solicitud in enumerate(
        solicitudes
    ):

        es_valida, errores = validar_solicitud(
            solicitud
        )

        # ----------------------------------------------------
        # Solicitud inválida
        # ----------------------------------------------------

        if not es_valida:

            id_solicitud = "DESCONOCIDO"

            if isinstance(
                solicitud,
                dict,
            ):
                id_solicitud = solicitud.get(
                    "id_solicitud",
                    "DESCONOCIDO",
                )

            resumen[
                "solicitudes_descartadas"
            ].append(
                {
                    "indice": indice,
                    "id_solicitud": id_solicitud,
                    "errores": errores,
                }
            )

            continue

        # ----------------------------------------------------
        # Solicitud válida
        # ----------------------------------------------------

        resumen[
            "solicitudes_validas"
        ].append(
            {
                "id_solicitud":
                    solicitud["id_solicitud"],

                "solicitante":
                    solicitud["solicitante"],

                "tipo":
                    solicitud["tipo"],

                "prioridad":
                    solicitud["prioridad"],

                "estado":
                    solicitud["estado"],

                "validado": True,
            }
        )

        prioridad = solicitud[
            "prioridad"
        ]

        estado = solicitud[
            "estado"
        ]

        tipo = solicitud[
            "tipo"
        ]

        minutos = float(
            solicitud[
                "minutos_atencion"
            ]
        )

        # ----------------------------------------------------
        # Distribución
        # ----------------------------------------------------

        resumen[
            "distribucion_prioridad"
        ][
            prioridad
        ] += 1

        resumen[
            "distribucion_estado"
        ][
            estado
        ] += 1

        resumen[
            "distribucion_tipo"
        ][
            tipo
        ] += 1

        minutos_validos.append(
            minutos
        )

        # ----------------------------------------------------
        # SLA
        # ----------------------------------------------------

        sla = SLA_POR_PRIORIDAD[
            prioridad
        ]

        if minutos > sla:

            resumen[
                "alertas_sla"
            ].append(
                {
                    "id_solicitud":
                        solicitud[
                            "id_solicitud"
                        ],

                    "prioridad":
                        prioridad,

                    "sla_minutos":
                        sla,

                    "minutos_atencion":
                        minutos,

                    "diferencia_minutos":
                        minutos - sla,
                }
            )

    # ========================================================
    # TOTALES
    # ========================================================

    total_validas = len(
        resumen[
            "solicitudes_validas"
        ]
    )

    total_descartadas = len(
        resumen[
            "solicitudes_descartadas"
        ]
    )

    total_recibidas = len(
        solicitudes
    )

    resumen[
        "resumen_general"
    ][
        "total_solicitudes_validas"
    ] = total_validas

    resumen[
        "resumen_general"
    ][
        "total_solicitudes_descartadas"
    ] = total_descartadas

    # --------------------------------------------------------
    # Porcentajes
    # --------------------------------------------------------

    if total_recibidas:

        resumen[
            "resumen_general"
        ][
            "tasa_aceptacion_porcentaje"
        ] = round(
            (
                total_validas
                / total_recibidas
            )
            * 100,
            2,
        )

        resumen[
            "resumen_general"
        ][
            "tasa_rechazo_porcentaje"
        ] = round(
            (
                total_descartadas
                / total_recibidas
            )
            * 100,
            2,
        )

    # --------------------------------------------------------
    # Métricas de tiempo
    # --------------------------------------------------------

    if minutos_validos:

        total_minutos = sum(
            minutos_validos
        )

        resumen[
            "metricas_tiempo"
        ][
            "promedio_minutos_atencion"
        ] = round(
            total_minutos
            / len(
                minutos_validos
            ),
            2,
        )

        resumen[
            "metricas_tiempo"
        ][
            "minutos_atencion_minimo"
        ] = min(
            minutos_validos
        )

        resumen[
            "metricas_tiempo"
        ][
            "minutos_atencion_maximo"
        ] = max(
            minutos_validos
        )

        resumen[
            "metricas_tiempo"
        ][
            "minutos_atencion_total"
        ] = total_minutos

    return resumen


# ============================================================
# MANEJO DE ARCHIVOS JSON
# ============================================================

def cargar_solicitudes_desde_json(
    ruta_archivo: str | Path,
) -> list[dict[str, Any]]:
    """
    Carga solicitudes desde un archivo JSON.

    Args:
        ruta_archivo:
            Ruta del archivo.

    Returns:
        Lista de solicitudes.

    Raises:
        FileNotFoundError
        json.JSONDecodeError
        ErrorProcesamientoSolicitudes
    """

    ruta = Path(
        ruta_archivo
    )

    if not ruta.exists():
        raise FileNotFoundError(
            f"Archivo no encontrado: {ruta}"
        )

    with ruta.open(
        "r",
        encoding="utf-8",
    ) as archivo:

        datos = json.load(
            archivo
        )

    if not isinstance(
        datos,
        list,
    ):
        raise ErrorProcesamientoSolicitudes(
            "El archivo JSON debe contener "
            "una lista de solicitudes"
        )

    return datos


def guardar_resumen_json(
    resumen: dict[str, Any],
    ruta_archivo: str | Path,
) -> None:
    """
    Guarda el resumen de procesamiento
    en un archivo JSON.
    """

    ruta = Path(
        ruta_archivo
    )

    ruta.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with ruta.open(
        "w",
        encoding="utf-8",
    ) as archivo:

        json.dump(
            resumen,
            archivo,
            indent=4,
            ensure_ascii=False,
        )


# ============================================================
# PRESENTACIÓN DE RESULTADOS
# ============================================================

def mostrar_resumen(
    resumen: dict[str, Any],
) -> None:
    """
    Presenta el resultado del procesamiento
    de forma legible en la consola.
    """

    general = resumen[
        "resumen_general"
    ]

    tiempo = resumen[
        "metricas_tiempo"
    ]

    print()

    print(
        "=" * 65
    )

    print(
        "     GESTOR DE SOLICITUDES "
        "FICTICIAS DE ATENCIÓN"
    )

    print(
        "=" * 65
    )

    print(
        "Solicitudes recibidas    :",
        general[
            "total_solicitudes_recibidas"
        ],
    )

    print(
        "Solicitudes válidas      :",
        general[
            "total_solicitudes_validas"
        ],
    )

    print(
        "Solicitudes descartadas  :",
        general[
            "total_solicitudes_descartadas"
        ],
    )

    print(
        "Tasa de aceptación       :",
        f"{general['tasa_aceptacion_porcentaje']}%",
    )

    print(
        "Tasa de rechazo          :",
        f"{general['tasa_rechazo_porcentaje']}%",
    )

    print(
        "Promedio atención        :",
        f"{tiempo['promedio_minutos_atencion']} "
        "minutos",
    )

    # --------------------------------------------------------
    # Prioridad
    # --------------------------------------------------------

    print()

    print(
        "Distribución por prioridad:"
    )

    for prioridad, cantidad in resumen[
        "distribucion_prioridad"
    ].items():

        print(
            f"  {prioridad:<10}: "
            f"{cantidad}"
        )

    # --------------------------------------------------------
    # Estado
    # --------------------------------------------------------

    print()

    print(
        "Distribución por estado:"
    )

    for estado, cantidad in resumen[
        "distribucion_estado"
    ].items():

        print(
            f"  {estado:<12}: "
            f"{cantidad}"
        )

    # --------------------------------------------------------
    # Alertas
    # --------------------------------------------------------

    if resumen[
        "alertas_sla"
    ]:

        print()

        print(
            "Alertas de SLA:"
        )

        for alerta in resumen[
            "alertas_sla"
        ]:

            print(
                "  "
                f"{alerta['id_solicitud']} | "
                f"{alerta['prioridad']} | "
                "exceso: "
                f"{alerta['diferencia_minutos']} min"
            )

    print(
        "=" * 65
    )


# ============================================================
# EJECUCIÓN PRINCIPAL
# ============================================================

def main() -> None:
    """
    Ejecuta el componente utilizando
    solicitudes_ejemplo.json.
    """

    ruta_base = (
        Path(__file__)
        .resolve()
        .parent
        .parent
    )

    ruta_datos = (
        ruta_base
        / "data"
        / "solicitudes_ejemplo.json"
    )

    ruta_resultado = (
        ruta_base
        / "data"
        / "resultado_procesamiento.json"
    )

    print(
        "Módulo gestor_solicitudes "
        "iniciado correctamente."
    )

    if not ruta_datos.exists():

        print(
            "No existe todavía el archivo "
            "de datos de ejemplo:"
        )

        print(
            ruta_datos
        )

        return

    try:

        solicitudes = (
            cargar_solicitudes_desde_json(
                ruta_datos
            )
        )

        resumen = procesar_solicitudes(
            solicitudes
        )

        mostrar_resumen(
            resumen
        )

        guardar_resumen_json(
            resumen,
            ruta_resultado,
        )

        print(
            "Resultado guardado en:",
            ruta_resultado,
        )

    except (
        FileNotFoundError,
        json.JSONDecodeError,
        ErrorProcesamientoSolicitudes,
    ) as error:

        print(
            "Error durante el procesamiento:",
            error,
        )


if __name__ == "__main__":
    main()
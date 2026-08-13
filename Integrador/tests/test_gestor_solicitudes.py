import json
from pathlib import Path

import pytest

from Integrador.src.gestor_solicitudes import (
    ErrorProcesamientoSolicitudes,
    cargar_solicitudes_desde_json,
    guardar_resumen_json,
    obtener_resumen_vacio,
    procesar_solicitudes,
    validar_coherencia_estado_tiempo,
    validar_coherencia_id_fecha,
    validar_estado,
    validar_fecha,
    validar_id_solicitud,
    validar_minutos_atencion,
    validar_prioridad,
    validar_solicitud,
    validar_solicitante,
    validar_tipo_solicitud,
)


# ============================================================
# PRUEBAS EXISTENTES - SE CONSERVAN
# ============================================================

def test_id_solicitud_valido_retorna_true():
    """Verifica que un identificador con formato válido sea aceptado."""
    valido, mensaje = validar_id_solicitud("SOL-20230415-001")
    assert valido is True
    assert mensaje == ""


def test_id_con_fecha_inexistente_retorna_false():
    """Verifica que una fecha inexistente dentro del identificador sea rechazada."""
    valido, mensaje = validar_id_solicitud("SOL-20230230-001")
    assert valido is False
    assert mensaje != ""


@pytest.mark.parametrize(
    "id_solicitud,esperado",
    [
        ("SOL-20260812-001", True),
        ("SOL-20260101-999", True),
        ("ABC-0001", False),
        ("SOL-20260230-001", False),
        ("SOL-20260812-01", False),
        ("", False),
        (None, False),
    ],
)
def test_validar_id_solicitud_parametrizado(id_solicitud, esperado):
    """Prueba parametrizada de identificadores válidos e inválidos."""
    valido, _ = validar_id_solicitud(id_solicitud)
    assert valido is esperado


def test_coherencia_id_fecha_correcta():
    """Verifica que la fecha incluida en el ID coincida con el campo fecha."""
    valido, mensaje = validar_coherencia_id_fecha(
        "SOL-20260812-001",
        "2026-08-12",
    )
    assert valido is True
    assert mensaje == ""


def test_coherencia_id_fecha_incorrecta():
    """Verifica que una diferencia entre ID y fecha sea detectada."""
    valido, mensaje = validar_coherencia_id_fecha(
        "SOL-20260812-001",
        "2026-08-13",
    )
    assert valido is False
    assert mensaje != ""


# ============================================================
# PRUEBAS AGREGADAS: VALIDADORES BÁSICOS
# ============================================================

@pytest.mark.parametrize(
    "validador,valor,esperado",
    [
        (validar_solicitante, "Usuario Ficticio", True),
        (validar_solicitante, "AB", False),
        (validar_solicitante, "A" * 101, False),
        (validar_solicitante, "@Usuario", False),
        (validar_solicitante, None, False),
        (validar_tipo_solicitud, "CONSULTA", True),
        (validar_tipo_solicitud, "URGENTE", False),
        (validar_prioridad, "ALTA", True),
        (validar_prioridad, None, False),
        (validar_estado, "ATENDIDA", True),
        (validar_estado, "FINALIZADA", False),
    ],
)
def test_validadores_basicos_parametrizado(validador, valor, esperado):
    """Prueba conjunto para solicitante, tipos, prioridad y estado."""
    valido, _ = validador(valor)
    assert valido is esperado


@pytest.mark.parametrize(
    "fecha,esperado",
    [
        ("2026-08-12", True),
        ("2026-8-12", False),
        ("2026-08-2", False),
        ("2024-02-29", True),
        ("2023-02-29", False),
        ("1949-12-31", False),
        ("2101-01-01", False),
        (None, False),
        ("2026-02-29", False),
        ("2026-13-01", False),
    ],
)
def test_validar_fecha_parametrizado(fecha, esperado):
    """Valida fechas normales, límite y formatos inválidos."""
    valido, _ = validar_fecha(fecha)
    assert valido is esperado


@pytest.mark.parametrize(
    "minutos,esperado",
    [
        (0, True),
        (35, True),
        (30.5, True),
        (-1, False),
        (10081, False),
        (None, False),
        ("60", False),
        (float("nan"), False),
    ],
)
def test_validar_minutos_atencion_parametrizado(minutos, esperado):
    """Verifica límites y valores no numéricos en minutos de atención."""
    valido, _ = validar_minutos_atencion(minutos)
    assert valido is esperado


@pytest.mark.parametrize(
    "id_solicitud,fecha,esperado",
    [
        ("SOL-20260812-001", "2026-08-12", True),
        ("SOL-20260812-001", "2026-08-13", False),
        ("SOL-20260812-001", "2026-09-12", False),
        ("ABC-20260812-001", "2026-08-12", False),
    ],
)
def test_validar_coherencia_id_fecha_parametrizado(id_solicitud, fecha, esperado):
    """Comprueba coherencia entre el identificador y la fecha."""
    valido, _ = validar_coherencia_id_fecha(id_solicitud, fecha)
    assert valido is esperado


@pytest.mark.parametrize(
    "estado,minutos,esperado",
    [
        ("REGISTRADA", 0, True),
        ("REGISTRADA", 1, False),
        ("EN_PROCESO", 120, True),
        ("ATENDIDA", 180, True),
    ],
)
def test_validar_coherencia_estado_tiempo_parametrizado(estado, minutos, esperado):
    """Comprueba la coherencia entre estado y tiempo de atención."""
    valido, _ = validar_coherencia_estado_tiempo(estado, minutos)
    assert valido is esperado


# ============================================================
# PRUEBAS AGREGADAS: VALIDACIÓN DE SOLICITUD COMPLETA
# ============================================================

def test_solicitud_completamente_valida():
    """Verifica que una solicitud perfectamente válida pase todas las reglas."""
    solicitud = {
        "id_solicitud": "SOL-20260812-001",
        "solicitante": "Usuario Ficticio",
        "fecha": "2026-08-12",
        "tipo": "CONSULTA",
        "prioridad": "BAJA",
        "estado": "ATENDIDA",
        "minutos_atencion": 35,
    }
    valido, errores = validar_solicitud(solicitud)
    assert valido is True
    assert errores == []


def test_solicitud_falta_campo_obligatorio():
    """Verifica que una solicitud sin campo obligatorio sea descartada."""
    solicitud = {
        "id_solicitud": "SOL-20260812-001",
        "solicitante": "Usuario Ficticio",
        "fecha": "2026-08-12",
        "tipo": "CONSULTA",
        "prioridad": "BAJA",
        "estado": "ATENDIDA",
    }
    valido, errores = validar_solicitud(solicitud)
    assert valido is False
    assert len(errores) > 0
    assert any("minutos_atencion" in error for error in errores)


def test_solicitud_con_incoherencia_detectada():
    """Verifica que la incoherencia entre ID y fecha sea reportada."""
    solicitud = {
        "id_solicitud": "SOL-20260812-001",
        "solicitante": "Usuario Ficticio",
        "fecha": "2026-08-13",
        "tipo": "CONSULTA",
        "prioridad": "BAJA",
        "estado": "ATENDIDA",
        "minutos_atencion": 35,
    }
    valido, errores = validar_solicitud(solicitud)
    assert valido is False
    assert any("coincide" in error.lower() for error in errores)


# ============================================================
# PRUEBAS AGREGADAS: RESUMEN Y PROCESAMIENTO
# ============================================================

def test_obtener_resumen_vacio():
    """Verifica la estructura estándar del resumen vacío."""
    resumen = obtener_resumen_vacio()
    assert isinstance(resumen, dict)
    assert "resumen_general" in resumen
    assert "metricas_tiempo" in resumen
    assert "distribucion_prioridad" in resumen
    assert "solicitudes_validas" in resumen
    assert "alertas_sla" in resumen
    assert resumen["resumen_general"]["total_solicitudes_recibidas"] == 0


def test_procesar_solicitudes_lista_vacia():
    """Verifica que una lista vacía se procese sin errores."""
    resumen = procesar_solicitudes([])
    assert resumen["resumen_general"]["total_solicitudes_recibidas"] == 0
    assert resumen["resumen_general"]["total_solicitudes_validas"] == 0
    assert resumen["resumen_general"]["total_solicitudes_descartadas"] == 0


def test_procesar_solicitudes_none_trata_como_vacio():
    """Verifica que None se interprete como lista vacía."""
    resumen = procesar_solicitudes(None)
    assert resumen["resumen_general"]["total_solicitudes_recibidas"] == 0


def test_procesar_solicitudes_no_lista_lanza_error():
    """Verifica que la entrada no lista lance ErrorProcesamientoSolicitudes."""
    with pytest.raises(ErrorProcesamientoSolicitudes):
        procesar_solicitudes("no es lista")


def test_procesar_solicitudes_mixta_generates_summary():
    """Verifica que una mezcla válida e inválida genere métricas y descartes."""
    solicitudes = [
        {
            "id_solicitud": "SOL-20260812-001",
            "solicitante": "Usuario Uno",
            "fecha": "2026-08-12",
            "tipo": "CONSULTA",
            "prioridad": "BAJA",
            "estado": "ATENDIDA",
            "minutos_atencion": 35,
        },
        {
            "id_solicitud": "INVALIDO",
            "solicitante": "Usuario Dos",
            "fecha": "2026-08-12",
            "tipo": "CONSULTA",
            "prioridad": "BAJA",
            "estado": "ATENDIDA",
            "minutos_atencion": 20,
        },
    ]
    resumen = procesar_solicitudes(solicitudes)
    assert resumen["resumen_general"]["total_solicitudes_recibidas"] == 2
    assert resumen["resumen_general"]["total_solicitudes_validas"] == 1
    assert resumen["resumen_general"]["total_solicitudes_descartadas"] == 1
    assert resumen["resumen_general"]["tasa_aceptacion_porcentaje"] == 50.0


# ============================================================
# PRUEBAS AGREGADAS: LECTURA Y ESCRITURA JSON
# ============================================================

def test_cargar_solicitudes_desde_json_archivo_valido():
    """Verifica que el archivo de ejemplo se cargue como lista de solicitudes."""
    solicitudes = cargar_solicitudes_desde_json(Path("Integrador/data/solicitudes_ejemplo.json"))
    assert isinstance(solicitudes, list)
    assert len(solicitudes) == 10


def test_cargar_solicitudes_desde_json_archivo_no_existe():
    """Verifica que un archivo inexistente lance FileNotFoundError."""
    ruta_inexistente = Path("Integrador/data/inexistente.json")
    with pytest.raises(FileNotFoundError):
        cargar_solicitudes_desde_json(ruta_inexistente)


def test_cargar_solicitudes_desde_json_no_es_lista(tmp_path):
    """Verifica que un JSON que no sea una lista lance ErrorProcesamientoSolicitudes."""
    archivo = tmp_path / "no_es_lista.json"
    archivo.write_text(json.dumps({"id": "valor"}), encoding="utf-8")
    with pytest.raises(ErrorProcesamientoSolicitudes):
        cargar_solicitudes_desde_json(archivo)


def test_guardar_resumen_json_crea_archivo(tmp_path):
    """Verifica que el resumen se guarde en un archivo temporal válido."""
    resumen = obtener_resumen_vacio()
    resumen["resumen_general"]["total_solicitudes_recibidas"] = 4
    archivo = tmp_path / "subdir" / "resumen.json"
    guardar_resumen_json(resumen, archivo)
    assert archivo.exists()
    contenido = json.loads(archivo.read_text(encoding="utf-8"))
    assert contenido["resumen_general"]["total_solicitudes_recibidas"] == 4


# ============================================================
# PRUEBA DE INTEGRACIÓN FINAL
# ============================================================

def test_integracion_final_solicitudes_ejemplo():
    """Carga el JSON real, valida y procesa las solicitudes con resultados esperados."""
    solicitudes = cargar_solicitudes_desde_json(Path("Integrador/data/solicitudes_ejemplo.json"))
    resumen = procesar_solicitudes(solicitudes)

    assert resumen["resumen_general"]["total_solicitudes_recibidas"] == 10
    assert resumen["resumen_general"]["total_solicitudes_validas"] == 5
    assert resumen["resumen_general"]["total_solicitudes_descartadas"] == 5
    assert resumen["resumen_general"]["tasa_aceptacion_porcentaje"] == 50.0
    assert resumen["resumen_general"]["tasa_rechazo_porcentaje"] == 50.0
    assert resumen["metricas_tiempo"]["promedio_minutos_atencion"] == 84.0
    assert len(resumen["alertas_sla"]) == 1
    assert resumen["alertas_sla"][0]["id_solicitud"] == "SOL-20260812-004"
    assert resumen["alertas_sla"][0]["prioridad"] == "CRITICA"
    assert resumen["alertas_sla"][0]["diferencia_minutos"] == 25

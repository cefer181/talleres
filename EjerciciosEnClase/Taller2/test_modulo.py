import pytest

from tramites import (
    validar_cedula,
    validar_fecha,
    clasificar_tiempo,
    calcular_promedio,
    resumen_diario,
)


# Verifica que una cédula de exactamente 10 dígitos numéricos sea válida.
def test_cedula_valida_retorna_true():
    assert validar_cedula("1234567890") is True


# Verifica que una cédula que contiene letras sea rechazada.
def test_cedula_con_letras_retorna_false():
    assert validar_cedula("12345A7890") is False


# Verifica que una fecha existente en formato dd/mm/aaaa sea válida.
def test_fecha_valida_retorna_true():
    assert validar_fecha("15/08/2023") is True


# Verifica que el 31 de febrero sea rechazado por ser una fecha inexistente.
def test_fecha_31_febrero_retorna_false():
    assert validar_fecha("31/02/2023") is False


# Verifica que exactamente 10 minutos se clasifiquen como Ágil.
def test_diez_minutos_es_agil():
    assert clasificar_tiempo(10) == "Ágil"


# Verifica que un tiempo negativo genere ValueError.
def test_tiempo_negativo_genera_error():
    with pytest.raises(ValueError):
        clasificar_tiempo(-5)


# Verifica el promedio de una lista normal de tiempos.
def test_promedio_tiempos_retorna_valor_correcto():
    tiempos = [10, 20, 30]
    assert calcular_promedio(tiempos) == 20.0


# Verifica que una lista vacía retorne un promedio de 0.0.
def test_promedio_lista_vacia_retorna_cero():
    assert calcular_promedio([]) == 0.0

    # Prueba varias cédulas válidas e inválidas utilizando parametrización.
@pytest.mark.parametrize("cedula, esperado", [
    ("1234567890", True),
    ("12345A7890", False),
    ("123456789", False),
    ("12345678901", False),
])
def test_validar_cedula_parametrizado(cedula, esperado):
    assert validar_cedula(cedula) == esperado

    # Prueba los valores límite de clasificación del tiempo de atención.
@pytest.mark.parametrize(
    "minutos,esperado",
    [
        (0, "Ágil"),
        (5, "Ágil"),
        (10, "Ágil"),
        (11, "Normal"),
        (30, "Normal"),
        (31, "Demorada"),
        (45, "Demorada"),
    ],
)
def test_clasificar_tiempo_parametrizado(minutos, esperado):
    assert clasificar_tiempo(minutos) == esperado

    # Prueba fechas válidas e inválidas, incluyendo casos límite del calendario.
@pytest.mark.parametrize(
    "fecha,esperado",
    [
        ("03/08/2026", True),
        ("01/01/1900", True),
        ("31/12/2100", True),
        ("31/02/2026", False),
        ("31/04/2026", False),
        ("01/13/2026", False),
        ("00/01/2026", False),
        ("03-08-2026", False),
    ],
)
def test_validar_fecha_parametrizada(fecha, esperado):
    assert validar_fecha(fecha) is esperado
# Gestor de Solicitudes Ficticias de Atención

## 1. Título e integrantes

- Proyecto: Gestor de Solicitudes Ficticias de Atención
- Integrantes:
  - César Jácome
  - Ximena Angulo

---

## 2. Introducción

Este proyecto implementa un gestor académico para validar, clasificar y procesar solicitudes ficticias de atención. El componente está desarrollado en Python y se centra en la validación de datos, la coherencia interna de la información y la generación de resúmenes operativos con métricas de atención.

La finalidad del caso integrador es demostrar el desarrollo de software con calidad, pruebas automatizadas y análisis estático, usando exclusivamente datos ficticios.

> Todos los datos utilizados en este proyecto son ficticios y no corresponden a personas, entidades ni registros reales.

---

## 3. Descripción del problema

En escenarios administrativos y de atención al usuario, es habitual recibir solicitudes con información incompleta, inconsistente o mal formateada. Si esos datos no se validan correctamente, se pueden procesar registros inválidos, generar métricas engañosas y comprometer la calidad del servicio.

El proyecto resuelve esta situación mediante la validación de cada solicitud, la detección de incoherencias, el descarte de registros inválidos y la generación de métricas de operación.

---

## 4. Justificación

La solución se justifica por la necesidad de aplicar buenas prácticas de programación y aseguramiento de la calidad en un caso académico basado en un flujo realista de validación de datos y análisis operativo.

Además, permite demostrar la utilidad de GitHub Copilot como apoyo al desarrollo, junto con testing automatizado y análisis estático con SonarQube for IDE.

---

## 5. Objetivo general

Desarrollar un gestor funcional para solicitudes ficticias de atención que valide, procese, clasifique y resuma información utilizando Python, datos ficticios, pruebas automatizadas y análisis estático de calidad.

---

## 6. Objetivos específicos

1. Validar campos obligatorios y formatos básicos.
2. Validar identificadores de solicitud con patrón realista.
3. Validar solicitantes con longitud y caracteres permitidos.
4. Validar fechas con formato estricto YYYY-MM-DD.
5. Validar tipos, prioridades y estados permitidos.
6. Validar tiempos de atención dentro de un rango lógico.
7. Detectar incoherencias entre ID y fecha.
8. Detectar incoherencias entre estado y tiempo de atención.
9. Procesar listas de solicitudes y descartar las inválidas.
10. Generar resúmenes y métricas de tiempo, distribución y SLA.
11. Cargar y guardar resultados en JSON.
12. Verificar el comportamiento mediante pruebas automatizadas.
13. Corregir defectos detectados por pytest y por SonarQube for IDE.

---

## 7. Alcance

El alcance del proyecto incluye:

- validación de una solicitud individual;
- validación de una colección de solicitudes;
- cálculo de métricas de desempeño;
- control de distribuciones por prioridad, estado y tipo;
- control de SLA por prioridad;
- carga desde JSON y escritura de resumen JSON;
- pruebas unitarias, parametrizadas, de límites y de integración;
- revisión humana de sugerencias de IA.

No se contempla un backend web ni persistencia real en base de datos. El proyecto es un módulo académico de validación y procesamiento en Python.

---

## 8. Arquitectura y estructura de carpetas

```text
Integrador/
├── README.md
├── PLAN_TRABAJO.md
├── requirements.txt
├── src/
│   └── gestor_solicitudes.py
├── tests/
│   └── test_gestor_solicitudes.py
├── data/
│   └── solicitudes_ejemplo.json
├── docs/
│   └── evidencias/
└── __init__.py (si aplica según entorno)
```

### Módulos principales

- src/gestor_solicitudes.py: módulo principal con validadores, reglas de coherencia, procesamiento y resumen.
- tests/test_gestor_solicitudes.py: baterías automatizadas de pruebas.
- data/solicitudes_ejemplo.json: conjunto ficticio de 10 solicitudes usado para verificación e integración.

---

## 9. Descripción de los datos

El archivo JSON de ejemplo contiene 10 solicitudes ficticias con una mezcla realista de casos válidos e inválidos. El contenido cubre:

- identificadores correctos e incorrectos;
- fechas válidas y no válidas;
- prioridades correctas e incorrectas;
- tiempos válidos e inválidos;
- estados permitidos y no permitidos;
- distintos tipos de solicitud;
- alerta SLA relacionada con prioridad CRITICA.

Cada registro está construido con datos inventados y no representa una entidad real.

---

## 10. Reglas funcionales

El módulo implementa las siguientes reglas:

- `id_solicitud` debe seguir el formato `SOL-YYYYMMDD-NNN`.
- La fecha incluida en el ID debe corresponder a una fecha real.
- `solicitante` debe existir, tener entre 3 y 100 caracteres y comenzar con una letra.
- `fecha` debe respetar el formato estricto `YYYY-MM-DD`.
- La fecha no puede ser anterior a 1950 ni posterior a 2100.
- `tipo` debe ser uno de: `CONSULTA`, `SOLICITUD`, `RECLAMO`, `INCIDENCIA`, `OTRO`.
- `prioridad` debe ser una de: `BAJA`, `MEDIA`, `ALTA`, `CRITICA`.
- `estado` debe ser uno de: `REGISTRADA`, `EN_PROCESO`, `ATENDIDA`, `CANCELADA`.
- `minutos_atencion` debe ser numérico, finito y estar entre 0 y 10080.
- `id_solicitud` y `fecha` deben ser coherentes.
- Si `estado` es `REGISTRADA`, no puede existir tiempo de atención acumulado.
- En caso de que la solicitud no sea válida, se descarta del procesamiento y se registra el motivo.

---

## 11. Prioridades, estados y tipos permitidos

### Prioridades

- BAJA
- MEDIA
- ALTA
- CRITICA

### Estados

- REGISTRADA
- EN_PROCESO
- ATENDIDA
- CANCELADA

### Tipos de solicitud

- CONSULTA
- SOLICITUD
- RECLAMO
- INCIDENCIA
- OTRO

---

## 12. SLA utilizado

El módulo usa un SLA ficticio expresado en minutos por prioridad:

| Prioridad | SLA (minutos) |
|---|---:|
| CRITICA | 60 |
| ALTA | 240 |
| MEDIA | 1440 |
| BAJA | 2880 |

Una solicitud genera una alerta cuando el tiempo de atención supera el límite de su prioridad.

---

## 13. Requisitos del entorno

- Python 3.12.10
- pytest 7.4.3
- pytest-cov 4.1.0
- Sistema operativo Windows 11
- No se requieren dependencias externas adicionales para la lógica principal

---

## 14. Instalación

1. Abrir el proyecto en el entorno de trabajo.
2. Ubicarse en la raíz del repositorio.
3. Crear un entorno virtual si se desea.
4. Instalar dependencias:

```bash
pip install -r Integrador/requirements.txt
```

---

## 15. Ejecución

Para ejecutar el módulo principal:

```bash
python Integrador/src/gestor_solicitudes.py
```

El módulo puede cargar datos ficticios desde JSON, validar solicitudes y mostrar un resumen de resultados.

---

## 16. Comandos principales

### Ejecutar pruebas

```bash
python -m pytest Integrador/tests/test_gestor_solicitudes.py -q
```

### Ejecutar pruebas con cobertura

```bash
python -m pytest Integrador/tests --cov=Integrador.src.gestor_solicitudes --cov-report=term-missing
```

### Ejecutar pruebas con salida detallada

```bash
python -m pytest Integrador/tests/test_gestor_solicitudes.py -v
```

---

## 17. Pruebas automatizadas

Se implementó una suite de pruebas automatizadas con pytest que incluye:

- pruebas unitarias;
- pruebas parametrizadas;
- pruebas de valores límite;
- pruebas de manejo de errores;
- pruebas de excepciones;
- pruebas sobre JSON y archivos temporales;
- pruebas de integración con solicitudes ficticias.

### Resultado real

- 61 casos efectivos recolectados.
- 61 casos PASSED.
- Python 3.12.10.
- pytest 7.4.3.
- pytest-cov 4.1.0.

---

## 18. Cobertura alcanzada

La cobertura del módulo principal reportada por pytest-cov fue:

- 79 % de cobertura del módulo `Integrador.src.gestor_solicitudes`

Esto refleja la evidencia real del proyecto en el entorno de ejecución utilizado.

---

## 19. Defecto identificado mediante pytest

Durante la ejecución de la batería, pytest detectó un defecto real en la validación de fechas. El caso fallaba al aceptar una fecha como:

```python
"2026-8-12"
```

La especificación exigía el formato estricto:

```python
YYYY-MM-DD
```

El defecto real fue que la función `validar_fecha` aceptaba fechas parcialmente formateadas. El equipo revisó críticamente la sugerencia inicial de cambiar la expectativa de la prueba y decidió mantener la prueba, corrigiendo la implementación.

---

## 20. Corrección aplicada

Se corrigió `validar_fecha` con una validación estricta de formato antes de realizar la conversión a fecha. Esta corrección garantizó que:

- solo se acepten fechas con formato `YYYY-MM-DD`;
- cadenas como `2026-8-12` y `2026-08-2` sean rechazadas;
- las fechas anteriores a 1950 y posteriores a 2100 sigan siendo rechazadas;
- la implementación quede alineada con la especificación funcional del proyecto.

La corrección fue validada con la ejecución exitosa completa de la batería de pruebas.

---

## 21. Análisis con SonarQube for IDE

Se ejecutó análisis estático del código propio con SonarQube for IDE.

### Estado inicial

- 5 hallazgos en código propio.
- 4 en `gestor_solicitudes.py`.
- 1 en `test_gestor_solicitudes.py`.

### Estado final

- 0 hallazgos en el código propio.

### Observación importante

Los 21 hallazgos visibles en `builtins.py` son externos al proyecto y no forman parte del código desarrollado en este caso integrador.

---

## 22. Comparación antes y después de SonarQube

| Aspecto | Estado inicial | Estado final |
|---|---:|---:|
| Hallazgos del proyecto | 5 | 0 |
| Hallazgos en gestor_solicitudes.py | 4 | 0 |
| Hallazgos en test_gestor_solicitudes.py | 1 | 0 |
| Hallazgos externos (builtins.py) | 21 | 21 |

La reducción de hallazgos del proyecto fue completa en el código propio, y el componente quedó limpio respecto a los elementos analizados.

---

## 23. Uso de GitHub Copilot

GitHub Copilot fue usado como apoyo durante distintas etapas del proyecto:

- revisión de la planificación;
- propuesta de diseño técnico;
- completions inline;
- apoyo en generación de pruebas;
- ampliación controlada de la batería de pruebas;
- análisis de errores;
- refactorización orientada a hallazgos SonarQube.

Todas las sugerencias fueron revisadas por el equipo antes de aceptarse.

---

## 24. Revisión humana de las sugerencias de IA

La revisión humana fue un componente crítico del flujo de trabajo. Se evaluó que cada sugerencia fuese coherente con la especificación y con la lógica del proyecto, evitando cambios que solo hicieran pasar una prueba sin respetar las reglas funcionales.

En particular, cuando se sugirió cambiar la expectativa de la prueba para aceptar una fecha inválida, el equipo decidió mantener la prueba original y corregir la implementación.

---

## 25. Estrategia Git

El proyecto se trabajó siguiendo una estrategia de ramas orientada a la trazabilidad:

- rama de desarrollo: `feature/caso-integrador`
- rama base: `main`
- el Pull Request todavía no ha sido creado

La estrategia buscó mantener trabajo organizado, revisado y controlado por fases.

---

## 26. Resultados finales

La ejecución funcional del proyecto dio los siguientes resultados reales:

- 10 solicitudes ficticias procesadas.
- 5 solicitudes válidas.
- 5 solicitudes descartadas.
- Tasa de aceptación: 50.0 %.
- Tasa de rechazo: 50.0 %.
- Promedio de atención: 84.0 minutos.
- Se generó una alerta SLA para `SOL-20260812-004`.
- Prioridad de la alerta: `CRITICA`.
- Exceso del SLA: 25 minutos.

Estos resultados se verificaron con la muestra real de ejemplo cargada desde el archivo JSON del proyecto.

---

## 27. Conclusiones

El proyecto cumple con los requisitos académicos y funcionales planteados. Se desarrolló una solución modular, verificable y documentada para el procesamiento de solicitudes ficticias de atención. La combinación entre pruebas automatizadas, detección de defectos, análisis estático y revisión humana permitió fortalecer la calidad del componente y demostrar un enfoque profesional de desarrollo.

Los puntos más relevantes fueron:

- la validación estricta de fechas;
- la capacidad de descartar elementos inválidos sin romper el flujo general;
- la generación de métricas y alertas por SLA;
- la resolución de hallazgos en SonarQube;
- la evidencia cuantificada de pruebas y cobertura.

---

## 28. Seguridad y confidencialidad

El proyecto fue diseñado con un enfoque de confidencialidad y uso responsable de la información:

- no se utilizan datos reales;
- los registros son ficticios y académicos;
- no se gestionan identificadores personales reales;
- la documentación y las pruebas no contienen información sensible;
- el proyecto se presenta como un caso de estudio técnico y formativo.

---

## 29. Declaración final sobre los datos

Todos los datos del proyecto son ficticios, diseñados exclusivamente con fines académicos y de validación técnica. No representan datos de clientes, usuarios ni organizaciones reales.

---

## 30. Cierre

El caso integrador se considera concluido en su etapa de análisis, implementación, pruebas y validación. El módulo principal, la suite automatizada y la documentación final evidencian una solución funcional, controlada y revisada, con resultados reales verificados y una calidad de código mejorada.


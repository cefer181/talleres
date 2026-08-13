# Plan de Trabajo - Gestor de Solicitudes Ficticias de Atención

## Introducción

Este documento recoge el desarrollo real del caso integrador, ajustado a los resultados verificados del proyecto. Se conserva la estructura por fases, pero cada una refleja el trabajo realizado, la evidencia aplicada y el estado real final del componente.

El proyecto fue desarrollado en Python con datos totalmente ficticios, validaciones rígidas, pruebas automatizadas y análisis estático con SonarQube for IDE. La ejecución final comprobó que la implementación cumple con la especificación y con los resultados esperados del caso.

---

## Fase 1: Definición y planificación

### Objetivo
Establecer los fundamentos conceptuales, funcionales y técnicos del proyecto.

### Actividades realizadas
- análisis del caso integrador;
- definición del problema y alcance;
- diseño del flujo de validación y procesamiento;
- selección de tecnologías y herramientas;
- definición del conjunto de datos ficticios;
- preparación de la documentación inicial.

### Resultado real
- ✅ README.md documentado con descripción, objetivos, alcance y reglas del proyecto.
- ✅ PLAN_TRABAJO.md definido y revisado.
- ✅ requirements.txt creado y validado.
- ✅ proyecto estructurado con carpetas src, tests, data y docs.

### Medio de verificación
- revisión de documentación técnica;
- validación de la estructura del proyecto;
- verificación de que el flujo propuesto es coherente con la implementación final.

---

## Fase 2: Desarrollo del componente

### Objetivo
Implementar la lógica principal del gestor de solicitudes ficticias.

### Actividades realizadas
- desarrollo de validaciones individuales;
- validación de campos obligatorios;
- validación de ID, solicitante, fecha, tipo, prioridad, estado y tiempo;
- implementación de reglas de coherencia entre ID-fecha y estado-tiempo;
- procesamiento de listas de solicitudes;
- cálculo de métricas y alertas SLA;
- carga y escritura de JSON.

### Resultado real
- ✅ `Integrador/src/gestor_solicitudes.py` implementado y funcional.
- ✅ validación completa de casos normales y anómalos.
- ✅ manejo de descartes y resúmenes de resultado.
- ✅ cumplimiento de la especificación funcional del caso.

### Medio de verificación
- ejecución directa del módulo;
- comprobación de validaciones con pruebas automatizadas;
- revisión de funciones y resultados generados.

---

## Fase 3: Generación de datos ficticios

### Objetivo
Crear un conjunto de datos representativo para pruebas y validación.

### Actividades realizadas
- diseño de un archivo JSON con 10 solicitudes ficticias;
- inclusión de casos válidos e inválidos;
- incorporación de inconsistencias intencionales;
- validación de la muestra real del caso integrador.

### Resultado real
- ✅ `Integrador/data/solicitudes_ejemplo.json` con 10 solicitudes ficticias.
- ✅ mezcla realista de casos válidos y descartados.
- ✅ todos los registros son inventados y no representan datos reales.

### Medio de verificación
- carga del archivo JSON con la función del módulo;
- comprobación de que el conjunto genera 5 válidas y 5 descartadas;
- validación del flujo final con resultados reales.

---

## Fase 4: Diseño de casos de prueba

### Objetivo
Definir la batería de pruebas que cubra validaciones, métricas y procesos completos.

### Actividades realizadas
- diseño de pruebas unitarias;
- diseño de pruebas parametrizadas;
- diseño de pruebas de valores límite;
- diseño de pruebas para errores y excepciones;
- diseño de pruebas de integración.

### Resultado real
- ✅ se definió una suite profesional y reducida, sin pruebas redundantes.
- ✅ se cubrieron validadores y flujo de procesamiento principal.
- ✅ se incluyó la prueba final con la muestra JSON real.

### Medio de verificación
- revisión de la suite implementada;
- validación de que cada área funcional estaba cubierta;
- comprobación de que se evitaban casos artificiales o redundantes.

---

## Fase 5: Pruebas automatizadas con pytest

### Objetivo
Ejecutar la suite real del proyecto y verificar calidad funcional.

### Actividades realizadas
- implementación de pruebas en `Integrador/tests/test_gestor_solicitudes.py`;
- uso de `pytest.mark.parametrize`;
- pruebas con None, cadenas vacías, tipos erróneos y archivos temporales;
- pruebas de integración sobre JSON real;
- ejecución de la suite completa.

### Resultado real
- ✅ 61 casos efectivos recolectados.
- ✅ 61 casos PASSED.
- ✅ Python 3.12.10.
- ✅ pytest 7.4.3.
- ✅ pytest-cov 4.1.0.

### Medio de verificación
```bash
python -m pytest Integrador/tests/test_gestor_solicitudes.py -q
```

Resultados verificados:
- 61 passed in 0.16s

---

## Fase 6: Análisis de resultados

### Objetivo
Evaluar la calidad de la implementación con evidencia real.

### Actividades realizadas
- revisión de resultados de pytest;
- comparación de métricas esperadas versus reales;
- identificación del defecto en formato de fecha;
- análisis de rendimiento del módulo y del flujo de procesamiento.

### Resultado real
- ✅ se confirmó el procesamiento final con 10 solicitudes, 5 válidas, 5 descartadas.
- ✅ tasa de aceptación 50.0 % y tasa de rechazo 50.0 %.
- ✅ promedio de atención 84.0 minutos.
- ✅ alerta SLA generada para `SOL-20260812-004` con prioridad CRITICA y exceso 25 minutos.

### Medio de verificación
- ejecución real de la suite;
- inspección del resumen final de procesamiento;
- validación de la alerta SLA y del promedio calculado.

---

## Fase 7: Corrección y refactorización

### Objetivo
Corregir defectos reales y mejorar la calidad del código sin cambiar el comportamiento funcional esperado.

### Actividades realizadas
- detección del defecto en `validar_fecha` al aceptar `2026-8-12`;
- revisión crítica de la recomendación inicial de adaptar la prueba;
- mantenimiento de la expectativa correcta y corrección de la función;
- ajuste de validación estricta con formato `YYYY-MM-DD`.

### Resultado real
- ✅ la validación de fecha quedó alineada con la especificación requerida.
- ✅ la batería de pruebas volvió a pasar completamente.
- ✅ no se cambiaron reglas funcionales ni resultados esperados.

### Medio de verificación
- ejecución repetida de pytest después de la corrección;
- validación de casos límite de fechas.

---

## Fase 8: Análisis de calidad y seguridad con SonarQube for IDE

### Objetivo
Revisar hallazgos del código propio para mejorar la calidad estática.

### Actividades realizadas
- análisis inicial de código del proyecto;
- identificación de 5 hallazgos: 4 en `gestor_solicitudes.py` y 1 en `test_gestor_solicitudes.py`;
- corrección de los 5 hallazgos;
- re-análisis del código propio.

### Resultado real
- ✅ estado inicial del código propio: 5 hallazgos.
- ✅ estado final del código propio: 0 hallazgos.
- ✅ 21 hallazgos visibles en `builtins.py` se mantienen como externos al proyecto.

### Medio de verificación
- análisis estático con SonarQube for IDE;
- revisión de correcciones realizadas en el módulo y la prueba;
- validación final de que no quedan hallazgos en código propio.

---

## Fase 9: Gestión de código con Git

### Objetivo
Mantener trazabilidad y organización del trabajo.

### Actividades realizadas
- uso de rama de desarrollo `feature/caso-integrador`;
- trabajo sobre rama distinta respecto a la base `main`;
- control del historial del proyecto;
- preparación para revisión final del caso integrador.

### Resultado real
- ✅ rama de trabajo definida y utilizada.
- ✅ rama base `main` no fue modificada con entregas directas.
- ✅ Pull Request todavía no creado.

### Medio de verificación
- revisión de estado del repositorio;
- confirmación del flujo de trabajo por ramas;
- validación del estado real de integración del proyecto.

---

## Fase 10: Pull Request final

### Objetivo
Preparar la entrega del proyecto en una rama de trabajo con revisión formal.

### Actividades realizadas
- consolidación del código y de la documentación;
- verificación funcional y de calidad;
- preparación para revisión final.

### Resultado real
- ✅ entregable funcional completo.
- ✅ pruebas y análisis correctos.
- ✅ PR todavía no creado.

### Medio de verificación
- revisión del estado del repositorio;
- comprobación de que la entrega está lista para revisión pero no se ha formalizado PR aún.

---

## Fase 11: Documentación técnica

### Objetivo
Documentar el proyecto de forma clara y profesional.

### Actividades realizadas
- actualización del README final;
- registro del proceso, resultados y defectos corregidos;
- documentación de uso, pruebas, cobertura y análisis de SonarQube.

### Resultado real
- ✅ documentación técnica actualizada con datos reales del proyecto.
- ✅ descripción de alcance, diseño, resultados y conclusiones.

### Medio de verificación
- revisión del contenido final del README;
- coherencia entre documentación y comportamiento ejecutado.

---

## Fase 12: Informe final

### Objetivo
Sintetizar resultados y evidencias del proyecto.

### Actividades realizadas
- registro de métricas reales;
- consolidación de resultados de pruebas y cobertura;
- registro de defectos corregidos y análisis de calidad.

### Resultado real
- ✅ resultados cuantificados y documentados;
- ✅ evidencias reales del proyecto incorporadas en la documentación.

### Medio de verificación
- comparación del contenido técnico con resultados ejecutados.

---

## Fase 13: Preparación para sustentación

### Objetivo
Preparar la presentación técnica y la defensa del proyecto.

### Actividades realizadas
- revisión del proyecto final con evidencia técnica;
- validación de resultados y pruebas;
- preparación del material conceptual y funcional para sustentación.

### Resultado real
- ✅ proyecto listo para presentar con resultados verificados.
- ✅ evidencia clara de pruebas, cobertura, validaciones y correcciones.

### Medio de verificación
- revisión final del proyecto con base en resultados reales y documentación actualizada.

---

## Resumen del estado real del proyecto

| Aspecto | Resultado real |
|---|---:|
| Solicitudes procesadas | 10 |
| Solicitudes válidas | 5 |
| Solicitudes descartadas | 5 |
| Tasa de aceptación | 50.0 % |
| Tasa de rechazo | 50.0 % |
| Promedio de atención | 84.0 minutos |
| Alerta SLA | 1 |
| ID con alerta | SOL-20260812-004 |
| Prioridad de alerta | CRITICA |
| Exceso del SLA | 25 minutos |
| Casos pytest recolectados | 61 |
| Casos PASSED | 61 |
| Cobertura módulo principal | 79 % |
| Hallazgos SonarQube código propio inicial | 5 |
| Hallazgos SonarQube código propio final | 0 |

---

## Criterios de éxito cumplidos

✅ La funcionalidad principal quedó implementada y validada.  
✅ La suite de pruebas pasó completamente.  
✅ Se corrigió un defecto real identificado por pytest.  
✅ Se resolvieron los hallazgos de SonarQube en el código propio.  
✅ La documentación final refleja el estado real del proyecto.  
✅ Los datos usados en todas las pruebas y en la muestra real son ficticios.  
✅ El proyecto mantiene una estructura técnica, profesional y académica.

---

**Versión**: 2.0  
**Última actualización**: 2026-08-12  
**Estado**: Proyecto finalizado con evidencia real, pruebas verificadas y documentación actualizada.

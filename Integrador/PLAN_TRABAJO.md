# Plan de Trabajo - Gestor de Solicitudes Ficticias de Atención

## Introducción

Este documento estructura el desarrollo del Caso Integrador en 13 fases secuenciales, cada una con objetivos claramente definidos, actividades concretas, resultados esperados y mecanismos de verificación.

---

## Fase 1: Definición y Planificación

### Objetivo

Establecer los fundamentos conceptuales, técnicos y operativos del proyecto mediante documentación clara y consenso en metodología.

### Actividades

1. Analizar el contexto y definir el problema a resolver
2. Establecer objetivos generales y específicos
3. Definir alcance funcional (features)
4. Diseñar estructura de datos (esquema de solicitud)
5. Seleccionar tecnologías y herramientas
6. Planificar fases de trabajo y cronograma
7. Establecer criterios de calidad y éxito
8. Definir estrategia de seguridad y confidencialidad

### Resultado Esperado

- ✅ README.md completado con descripción, objetivos y alcance
- ✅ PLAN_TRABAJO.md completado (este documento)
- ✅ requirements.txt con dependencias iniciales
- ✅ Documento de consenso en metodología y herramientas
- ✅ Estructura de datos finalizada y validada

### Medio de Verificación

- Revisión de README.md: Contiene todos los elementos solicitados
- Revisión de PLAN_TRABAJO.md: Detalles de todas las 13 fases
- requirements.txt existe y es coherente
- Documentación aceptada por ambos integrantes

---

## Fase 2: Desarrollo del Componente Asistido con GitHub Copilot

### Objetivo

Implementar la lógica funcional principal del gestor de solicitudes utilizando GitHub Copilot como asistente de codificación.

### Actividades

1. Crear clase principal `GestorSolicitudes` con estructura básica
2. Implementar validadores de campos obligatorios
3. Implementar validadores de identificadores (ID de solicitud, ID de cliente)
4. Implementar validadores de fechas
5. Implementar validadores de prioridades
6. Implementar validadores de estados
7. Implementar validadores de tiempos de atención
8. Implementar detector de inconsistencias
9. Implementar clasificador de solicitudes
10. Implementar funciones de cálculo de métricas
11. Implementar generador de reportes/resúmenes
12. Refactorizar código para mejorar legibilidad

### Resultado Esperado

- ✅ src/gestor_solicitudes.py completado con todas las funciones
- ✅ Código modular y reutilizable
- ✅ Funciones con docstrings explicativos
- ✅ Manejo de excepciones implementado
- ✅ Logging de auditoría incorporado

### Medio de Verificación

- Verificación de que todas las funciones requieren están implementadas
- Ejecución manual de funciones para validar comportamiento básico
- Revisión de docstrings en cada función
- Análisis de complejidad de código

---

## Fase 3: Generación de Datos Ficticios

### Objetivo

Crear un conjunto de datos ficticios realista para validar y probar el componente de gestión.

### Actividades

1. Diseñar estructura de solicitudes_ejemplo.json
2. Generar 30-50 solicitudes ficticias variadas:
   - Con todos los campos válidos
   - Con campos faltantes
   - Con valores inválidos (para testing negativo)
   - Con inconsistencias (fechas invertidas, etc.)
3. Validar coherencia de datos ficticios
4. Documentar casos especiales en dataset
5. Crear dataset adicional para casos límite si es necesario

### Resultado Esperado

- ✅ data/solicitudes_ejemplo.json contiene 30-50 registros
- ✅ Incluye casos válidos e inválidos
- ✅ Datos completamente ficticios (sin información real)
- ✅ Estructura coherente con esquema definido en Fase 1
- ✅ Documentación de intención de cada registro

### Medio de Verificación

- Validar JSON está bien formado (sintaxis correcta)
- Verificar que no contiene datos personales reales
- Revisar que existen casos variados (válidos/inválidos/límite)
- Cargar datos en gestor para validación básica

---

## Fase 4: Diseño de Casos de Prueba

### Objetivo

Especificar exhaustivamente qué será probado y cómo, antes de implementar las pruebas.

### Actividades

1. Diseñar casos de prueba para cada validador:
   - Entrada válida
   - Entrada nula/vacía
   - Tipo de dato incorrecto
   - Valores límite
   - Valores inválidos específicos

2. Diseñar casos de prueba para clasificación:
   - Cada categoría posible
   - Casos ambiguos

3. Diseñar casos de prueba para métricas:
   - Conjunto vacío
   - Un único registro
   - Múltiples registros
   - Registros descartados vs. válidos

4. Diseñar casos de prueba de integración:
   - Flujo completo de carga → validación → clasificación → métricas
   - Manejo de errores durante procesamiento

5. Documentar caso de prueba en formato:
   - Nombre descriptivo
   - Objetivo
   - Entrada
   - Salida esperada
   - Aserciones

### Resultado Esperado

- ✅ Documento con especificación de ≥40 casos de prueba
- ✅ Cobertura de todas las funciones principales
- ✅ Clasificación clara de pruebas (unitarias/integración)
- ✅ Criterios de aceptación definidos
- ✅ Casos límite documentados

### Medio de Verificación

- Revisar documento de casos de prueba
- Validar que cada función tiene mínimo 3 casos
- Verificar que existen casos de éxito y fracaso
- Confirmar cobertura estimada ≥ 80%

---

## Fase 5: Pruebas Unitarias e Integración con pytest

### Objetivo

Implementar suite completa de pruebas automatizadas en pytest basada en diseño de Fase 4.

### Actividades

1. Configurar pytest en proyecto
2. Crear estructura de tests en tests/test_gestor_solicitudes.py
3. Implementar fixtures para datos de prueba
4. Implementar pruebas unitarias para cada validador
5. Implementar pruebas para clasificador
6. Implementar pruebas para cálculo de métricas
7. Implementar pruebas de integración
8. Implementar pruebas de manejo de excepciones
9. Ejecutar pruebas y validar cobertura
10. Refactorizar tests si es necesario

### Resultado Esperado

- ✅ tests/test_gestor_solicitudes.py contiene ≥40 pruebas
- ✅ Todos los tests pasan
- ✅ Cobertura de código ≥ 80%
- ✅ Tests son independientes y reutilizables
- ✅ Reporte de cobertura generado (pytest-cov)

### Medio de Verificación

```bash
pytest tests/ -v --cov=src --cov-report=html
```

- Ejecutar comando anterior: todos los tests deben pasar
- Archivo htmlcov/index.html muestra cobertura ≥ 80%
- Revisar tests para asegurar que son significativos

---

## Fase 6: Análisis de Resultados

### Objetivo

Evaluar los resultados de testing y extraer conclusiones sobre la funcionalidad del componente.

### Actividades

1. Analizar resultados de pruebas unitarias
2. Identificar funciones con baja cobertura
3. Evaluar casos límite que fallaron
4. Documentar comportamientos inesperados
5. Calcular métricas de calidad:
   - % de pruebas pasadas
   - Cobertura de líneas
   - Complejidad de funciones
6. Crear reporte de hallazgos
7. Identificar áreas de mejora

### Resultado Esperado

- ✅ Documento de análisis de resultados con:
  - Resumen ejecutivo
  - Métricas de testing
  - Casos problemáticos identificados
  - Recomendaciones de mejora
- ✅ Gráficos o tablas de cobertura
- ✅ Lista priorizada de issues a resolver

### Medio de Verificación

- Revisar documento de análisis
- Validar que identifica correctamente areas de mejora
- Confirmar que métricas se basan en resultados reales
- Verificar que recomendaciones son accionables

---

## Fase 7: Corrección y Refactorización

### Objetivo

Mejorar el código identificado en Fase 6, aumentando calidad, mantenibilidad y robustez.

### Actividades

1. Resolver issues identificados en pruebas fallidas
2. Mejorar cobertura de código (target: 85%+)
3. Simplificar funciones complejas (reduce complejidad ciclomática)
4. Eliminar código duplicado
5. Mejorar nombres de variables y funciones
6. Optimizar rendimiento si es necesario
7. Mejorar manejo de excepciones
8. Actualizar docstrings si cambió lógica
9. Re-ejecutar tests completos
10. Actualizar reporte de cobertura

### Resultado Esperado

- ✅ Cobertura de código ≥ 85%
- ✅ Complejidad ciclomática < 10 para todas las funciones
- ✅ Duplicación de código < 5%
- ✅ Todos los tests siguen pasando
- ✅ Código más legible y mantenible

### Medio de Verificación

```bash
pytest tests/ -v --cov=src --cov-report=html
```

- Cobertura reportada ≥ 85%
- Revisar código para verificar legibilidad
- Comparar complejidad antes/después

---

## Fase 8: Análisis de Calidad y Seguridad con SonarQube for IDE

### Objetivo

Ejecutar análisis estático de código para identificar vulnerabilidades, problemas de calidad y deuda técnica.

### Actividades

1. Instalar y configurar SonarQube for IDE en VS Code
2. Ejecutar análisis local en src/gestor_solicitudes.py
3. Ejecutar análisis en tests/test_gestor_solicitudes.py
4. Revisar resultados de análisis:
   - Bugs
   - Vulnerabilidades de seguridad
   - Security Hotspots
   - Code Smells
   - Complejidad
5. Crear plan de remediación
6. Resolver problemas críticos
7. Documentar problemas no resueltos (con justificación)
8. Re-ejecutar análisis para confirmar mejoras

### Resultado Esperado

- ✅ Análisis SonarQube completado sin errores de ejecución
- ✅ Cero vulnerabilidades críticas
- ✅ Cero bugs críticos
- ✅ Documentación de Security Hotspots revisada
- ✅ Documento de remediación con acciones tomadas
- ✅ Pantallazos de análisis guardados en docs/evidencias/

### Medio de Verificación

- Pantallazos de interfaz de SonarQube mostrando resultados
- Documento de remediación con cambios realizados
- Verificación de que problemas críticos fueron resueltos
- Re-análisis confirma mejoras

---

## Fase 9: Gestión de Código mediante Git y GitHub

### Objetivo

Organizar historial de cambios, mantener trazabilidad y preparar repositorio para colaboración.

### Actividades

1. Inicializar repositorio Git (si no existe)
2. Crear estructura de branches según plan:
   - `main` (principal, código estable)
   - `develop` (rama de integración)
   - Ramas de feature para cada funcionalidad
3. Hacer commits significativos con mensajes claros:
   - Formato convencional (feat:, fix:, docs:, test:, refactor:, etc.)
   - Cada commit debe ser atómico y funcional
4. Integrar cambios en `develop` mediante PRs
5. Documentar proceso en CONTRIBUTING.md si es necesario
6. Configurar GitHub para:
   - Requerir revisión en PRs
   - Ejecutar tests automáticos
   - Bloquear merge si tests fallan

### Resultado Esperado

- ✅ Repositorio con estructura clara de branches
- ✅ Historial de commits bien documentado
- ✅ Mínimo 10-15 commits significativos
- ✅ Rama `develop` con código integrado
- ✅ Rama `main` lista para release

### Medio de Verificación

```bash
git log --oneline
git branch -a
```

- Verificar estructura de branches
- Revisar historial de commits en GitHub/GitLab
- Confirmar que mensajes de commit son descriptivos

---

## Fase 10: Pull Request Final

### Objetivo

Consolidar el trabajo en una Pull Request de integración a rama principal con revisión formal.

### Actividades

1. Asegurar que `develop` contiene código completo y probado
2. Crear PR desde `develop` hacia `main`
3. Completar plantilla de PR con:
   - Descripción de cambios
   - Conexión a issues/objetivos
   - Cambios realizados por fase
   - Testing realizado
   - Pantallazos de ejecución
4. Solicitar revisión de pares (mínimo 1 revisor)
5. Responder comentarios y sugerencias
6. Resolver conflictos si existen
7. Obtener aprobación de revisores
8. Ejecutar checks finales (tests, análisis)
9. Hacer merge a `main`
10. Crear release tag (v1.0)

### Resultado Esperado

- ✅ PR creado en GitHub/GitLab
- ✅ Descripción completa y clara
- ✅ Revisión realizada y aprobada
- ✅ Merge a `main` completado
- ✅ Release tag v1.0 creado
- ✅ Historial visible en GitHub

### Medio de Verificación

- URL de PR pública y accesible
- Revisión registrada de al menos 1 revisor
- Comentarios/conversación documentados
- Merge commit registrado en `main`

---

## Fase 11: Documentación Técnica

### Objetivo

Crear documentación completa que permita entender, usar y mantener el componente.

### Actividades

1. Crear docs/ARQUITECTURA.md:
   - Diagrama de arquitectura
   - Descripción de módulos
   - Flujos de datos

2. Crear docs/GUIA_USO.md:
   - Instalación
   - Uso básico con ejemplos
   - API de funciones

3. Crear docs/CASOS_PRUEBA.md:
   - Especificación de todos los casos de prueba
   - Matriz de cobertura

4. Crear docs/DECISIONES_TECNICAS.md:
   - Por qué se eligieron ciertas tecnologías
   - Alternativas consideradas y descartadas
   - Trade-offs

5. Crear docs/LECCIONES_APRENDIDAS.md:
   - Desafíos enfrentados
   - Soluciones implementadas
   - Mejoras sugeridas para trabajo futuro

6. Actualizar README.md si es necesario
7. Guardar evidencias de proceso en docs/evidencias/:
   - Pantallazos de testing
   - Pantallazos de análisis SonarQube
   - Logs de ejecución

### Resultado Esperado

- ✅ docs/ARQUITECTURA.md completado
- ✅ docs/GUIA_USO.md con ejemplos funcionales
- ✅ docs/CASOS_PRUEBA.md con matriz de cobertura
- ✅ docs/DECISIONES_TECNICAS.md completo
- ✅ docs/LECCIONES_APRENDIDAS.md con insights
- ✅ docs/evidencias/ contiene pantallazos y logs

### Medio de Verificación

- Revisar que cada documento tiene contenido sustancial
- Validar que ejemplos son ejecutables
- Verificar que documentación es coherente con código
- Confirmar que evidencias están organizadas

---

## Fase 12: Elaboración del Informe

### Objetivo

Preparar documento formal que sintetice todo el trabajo realizado y resultados obtenidos.

### Actividades

1. Crear INFORME_FINAL.md con estructura:
   - Portada (título, integrantes, fecha, institución)
   - Tabla de contenidos
   - Resumen ejecutivo (1 página)
   - Introducción y contexto
   - Objetivos (reiterados del README)
   - Metodología utilizada
   - Desarrollo (una sección por fase importante)
   - Resultados obtenidos (con métricas)
   - Análisis de resultados
   - Conclusiones
   - Recomendaciones futuras
   - Anexos (código, pantallazos, logs)
   - Referencias

2. Incluir métricas cuantitativas:
   - Líneas de código
   - Cobertura de testing
   - Número de pruebas
   - Tiempo invertido por fase
   - Hallazgos de SonarQube

3. Incluir pantallazos y diagramas
4. Revisar coherencia y ortografía
5. Obtener validación de pares

### Resultado Esperado

- ✅ INFORME_FINAL.md de 15-25 páginas (completo)
- ✅ Resumen ejecutivo claro
- ✅ Métricas cuantificables
- ✅ Evidencia de todo el trabajo realizado
- ✅ Lenguaje técnico, académico y profesional

### Medio de Verificación

- Revisar estructura del informe
- Validar que métricasse basan en datos reales
- Confirmar que todas las fases están representadas
- Revisar ortografía y formato

---

## Fase 13: Preparación de la Sustentación

### Objetivo

Preparar presentación clara y convincente del proyecto para audiencia evaluadora.

### Actividades

1. Crear presentación (slides) que incluya:
   - Portada (título, integrantes)
   - Problema y contexto (1-2 slides)
   - Objetivos y alcance (1-2 slides)
   - Metodología (1 slide)
   - Arquitectura/diseño (2-3 slides)
   - Desarrollo y proceso (2-3 slides)
   - Resultados de testing (2 slides)
   - Análisis SonarQube (1-2 slides)
   - Demostración en vivo (2-3 slides)
   - Lecciones aprendidas (1 slide)
   - Conclusiones y futuro (1 slide)

2. Preparar demostración en vivo:
   - Ejecución de aplicación
   - Ejecución de pruebas
   - Muestra de cobertura
   - Ejecución de análisis SonarQube

3. Preparar guion/speaker notes
4. Practicar presentación (mínimo 2 veces)
5. Preparar respuestas a preguntas frecuentes
6. Verificar que todos los equipos/herramientas funcionan

### Resultado Esperado

- ✅ Presentación en formato PowerPoint/Google Slides (10-15 slides)
- ✅ Demo script documentado
- ✅ Speaker notes completos
- ✅ Respuestas preparadas a preguntas técnicas
- ✅ Ensayo realizado mínimo 2 veces

### Medio de Verificación

- Revisar presentación para claridad
- Ejecutar demo completa sin errores
- Cronometrar duración (debe ser ≤ 15-20 minutos)
- Validar que responde preguntas probables

---

## Resumen de Entregas por Fase

| Fase | Entregable | Responsabilidad |
|------|-----------|-----------------|
| 1 | README.md, PLAN_TRABAJO.md, requirements.txt | Conjunta |
| 2 | src/gestor_solicitudes.py | Asistida por Copilot |
| 3 | data/solicitudes_ejemplo.json | Conjunta |
| 4 | Especificación de casos de prueba | Conjunta |
| 5 | tests/test_gestor_solicitudes.py | Asistida por Copilot |
| 6 | Documento de análisis de resultados | Análisis conjunto |
| 7 | Código refactorizado | Mejoras conjuntas |
| 8 | Análisis SonarQube + remediación | Análisis conjunto |
| 9 | Repositorio Git bien organizado | Configuración conjunta |
| 10 | Pull Request a `main` + merge | Revisión conjunta |
| 11 | Documentación en docs/ | Redacción conjunta |
| 12 | INFORME_FINAL.md | Redacción conjunta |
| 13 | Presentación + demo | Preparación conjunta |

---

## Criterios de Éxito General

El proyecto se considerará exitoso cuando:

✅ Todas las funcionalidades especificadas están implementadas y funcionan correctamente  
✅ Cobertura de tests es ≥ 85%  
✅ SonarQube no reporta vulnerabilidades críticas  
✅ Código está bien documentado y es mantenible  
✅ Historial de Git es claro y trazable  
✅ Informe es completo y profesional  
✅ Presentación es clara y demuestra conocimiento profundo  
✅ Datos utilizados son 100% ficticios  
✅ Equipo trabajó colaborativamente  

---

**Versión**: 1.0  
**Última actualización**: 2026-08-12  
**Estado**: Plan completo, listo para ejecución

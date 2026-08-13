# Gestor de Solicitudes Ficticias de Atención

## Integrantes del Proyecto

- **César Jácome**
- **Ximena Angulo**

---

## Descripción del Problema

En contextos empresariales y administrativos, la gestión eficiente de solicitudes de atención es crítica para mantener la satisfacción del usuario y optimizar recursos. Sin embargo, los sistemas de gestión de solicitudes frecuentemente enfrentan desafíos tales como:

1. **Validación inconsistente** de datos de entrada
2. **Falta de clasificación** automática según prioridad y naturaleza de la solicitud
3. **Impossibilidad de detectar registros inconsistentes** o malformados
4. **Ausencia de métricas** para analizar el desempeño del servicio
5. **Dificultad en la auditabilidad** del procesamiento de solicitudes

Este proyecto aborda estos desafíos mediante el desarrollo de un componente funcional que automatiza la validación, clasificación y procesamiento de solicitudes.

---

## Justificación

El desarrollo de un **Gestor de Solicitudes Ficticias de Atención** es justificado por:

1. **Necesidad de validación robusta**: Garantizar que solo solicitudes válidas sean procesadas
2. **Optimización operativa**: Automatizar tareas repetitivas de validación y clasificación
3. **Generación de inteligencia de negocio**: Producir métricas y análisis del desempeño
4. **Mejora de calidad de código**: Aplicar prácticas profesionales de desarrollo asistido con IA
5. **Aseguramiento de la calidad**: Implementar estrategias rigurosas de testing y análisis estático

---

## Objetivo General

Desarrollar un componente funcional en Python que simule la recepción, validación, clasificación y procesamiento de solicitudes ficticias de atención, aplicando prácticas profesionales de desarrollo asistido con GitHub Copilot y aseguramiento de la calidad mediante pruebas automatizadas y análisis de código.

---

## Objetivos Específicos

1. **Validación de campos obligatorios**: Garantizar que todas las solicitudes contengan información requerida
2. **Validación de identificadores ficticios**: Verificar formatos y coherencia de IDs de solicitud y cliente
3. **Validación de fechas**: Asegurar que las fechas sean válidas y coherentes
4. **Validación de prioridades**: Verificar que las prioridades se ajusten a valores permitidos
5. **Validación de estados**: Confirmar que los estados de solicitud sean válidos
6. **Validación de tiempos de atención**: Verificar que los tiempos cumplan criterios de plausibilidad
7. **Detección de registros inconsistentes**: Identificar y descartar solicitudes con datos contradictorios
8. **Clasificación de solicitudes**: Categorizar solicitudes según criterios predefinidos
9. **Generación de métricas**: Calcular totales, promedios y estadísticas de desempeño
10. **Creación de reportes**: Generar resúmenes ejecutivos del procesamiento

---

## Alcance Funcional

### Funcionalidades Previstas

El componente `gestor_solicitudes` implementará las siguientes funcionalidades:

- **Carga de datos**: Importar solicitudes desde archivos JSON
- **Validación integral**: Ejecutar todas las validaciones descritas en objetivos específicos
- **Limpieza de datos**: Descartar solicitudes inválidas con registro del motivo
- **Clasificación automática**: Asignar categorías a solicitudes válidas
- **Cálculo de métricas**:
  - Total de solicitudes válidas procesadas
  - Total de solicitudes descartadas
  - Promedio de tiempo de atención
  - Distribución por prioridad
  - Distribución por estado
  - Tasa de rechazo
- **Generación de reportes**: Producir salidas estructuradas (JSON, diccionarios Python)
- **Auditabilidad**: Mantener trazabilidad de decisiones de validación

---

## Estructura de Datos Propuesta

### Esquema de una Solicitud

Una solicitud de atención tendrá la siguiente estructura JSON:

```json
{
  "id_solicitud": "SOL-20260812-001",
  "id_cliente": "CLI-FIC-0042",
  "fecha_creacion": "2026-08-12T09:30:00Z",
  "fecha_vencimiento": "2026-08-19T23:59:59Z",
  "asunto": "Consulta técnica sobre funcionalidad del sistema",
  "descripcion": "Se requiere asistencia para configurar el módulo de reportes...",
  "prioridad": "MEDIA",
  "estado": "EN_PROCESO",
  "categoria": "SOPORTE_TECNICO",
  "tiempo_atension_horas": 4.5,
  "asignado_a": "AGENTE-003",
  "notas_internas": "Cliente VIP, atender con preferencia"
}
```

### Campos Obligatorios

- `id_solicitud`
- `id_cliente`
- `fecha_creacion`
- `fecha_vencimiento`
- `asunto`
- `prioridad`
- `estado`
- `tiempo_atension_horas`

### Campos Opcionales

- `descripcion`
- `categoria`
- `asignado_a`
- `notas_internas`

---

## Prioridades Permitidas

```python
PRIORIDADES_VALIDAS = {
    "BAJA": 1,
    "MEDIA": 2,
    "ALTA": 3,
    "CRITICA": 4
}
```

---

## Estados Permitidos

```python
ESTADOS_VALIDOS = {
    "PENDIENTE",
    "EN_PROCESO",
    "RESUELTA",
    "CERRADA",
    "RECHAZADA"
}
```

---

## Categorías de Clasificación

```python
CATEGORIAS_VALIDAS = {
    "SOPORTE_TECNICO",
    "FACTURACION",
    "CUENTA",
    "PRODUCTO",
    "OTROS"
}
```

---

## Tecnologías Utilizadas

### Lenguaje y Framework

- **Python 3.8+**: Lenguaje principal de desarrollo
- **Estándar POSIX**: Para operaciones de archivo y sistema

### Dependencias de Producción

- (Ninguna dependencia externa requerida para la Fase 1 - se utilizan módulos estándar)

### Dependencias de Desarrollo y Testing

- **pytest**: Framework de pruebas unitarias
- **pytest-cov**: Plugin para cobertura de código

### Herramientas de Análisis y Calidad

- **GitHub Copilot**: Asistencia en codificación
- **SonarQube for IDE**: Análisis estático de código (Local Code Analysis)
- **Git/GitHub**: Control de versiones y colaboración

---

## Estructura del Proyecto

```
Integrador/
├── README.md                           # Este archivo
├── PLAN_TRABAJO.md                     # Plan de trabajo detallado
├── requirements.txt                    # Dependencias del proyecto
├── src/
│   └── gestor_solicitudes.py           # Módulo principal del gestor
├── tests/
│   └── test_gestor_solicitudes.py      # Suite de pruebas unitarias
├── data/
│   └── solicitudes_ejemplo.json        # Datos ficticios para testing
└── docs/
    └── evidencias/                     # Documentación y evidencias de proceso
```

### Descripción de Directorios

- **src/**: Código fuente del componente funcional
- **tests/**: Casos de prueba y suite de testing
- **data/**: Datos ficticios utilizados en validación y testing
- **docs/**: Documentación técnica y evidencias del desarrollo

---

## Metodología de Trabajo

### Enfoque de Desarrollo

1. **Desarrollo Asistido con IA**: Utilizar GitHub Copilot como asistente principal para acelerar codificación y generar propuestas de solución
2. **Test-Driven Development (TDD)**: Diseñar casos de prueba antes de implementar funcionalidad
3. **Iterativo e Incremental**: Desarrollar en ciclos cortos con validación continua
4. **Pair Programming**: Revisar mutuamente el código generado y las decisiones

### Colaboración

- **Rama principal (`main`)**: Código estable y probado
- **Rama de desarrollo (`develop`)**: Rama base para features
- **Ramas de feature**: `feature/validacion-campos`, `feature/clasificacion`, etc.
- **Pull Requests**: Requieren revisión de pares antes de merge

---

## Estrategia de Pruebas

### Niveles de Testing

1. **Pruebas Unitarias**: Validar cada función de manera aislada
   - Validación de campos individuales
   - Lógica de clasificación
   - Cálculo de métricas

2. **Pruebas de Integración**: Validar el flujo completo de procesamiento
   - Carga de datos → Validación → Clasificación → Métricas

3. **Pruebas de Caso Límite**: Validar comportamiento en escenarios extremos
   - Datos vacíos
   - Valores nulos
   - Strings especiales
   - Fechas inválidas
   - Números negativos/cero

### Framework y Herramientas

- **pytest**: Framework de testing
- **pytest-cov**: Medición de cobertura de código
- **Objetivo de cobertura**: Mínimo 80% de cobertura de líneas

### Estrategia de Test Data

- Datos ficticios completamente inventados
- Casos válidos y casos inválidos
- Casos límite y anomalías

---

## Uso Previsto de GitHub Copilot

### Aplicaciones Planificadas

1. **Generación de código boilerplate**: Estructura base de funciones y clases
2. **Implementación de validadores**: Funciones de validación de campos
3. **Lógica de clasificación**: Algoritmos de categorización
4. **Cálculo de métricas**: Funciones de agregación y estadística
5. **Generación de pruebas**: Casos de prueba unitarios y de integración
6. **Documentación de código**: Docstrings y comentarios explicativos

### Restricciones de Uso

- ✅ Usar para acelerar desarrollo
- ✅ Generar propuestas que revisaremos críticamente
- ❌ No aceptar código sin comprensión
- ❌ No utilizar soluciones inseguras o de baja calidad
- ❌ No generar datos reales en ejemplos

---

## Análisis de Calidad y Seguridad con SonarQube for IDE

### Métricas a Evaluar

1. **Cobertura de código**: Mínimo 80%
2. **Duplicación de código**: < 5%
3. **Complejidad ciclomática**: < 10 por método
4. **Code smells**: Ninguno crítico
5. **Vulnerabilidades**: Cero
6. **Security hotspots**: Revisión manual completa

### Tipos de Análisis

- **Análisis Local (on-the-fly)**: Validación en tiempo de desarrollo
- **Análisis Conectado (Connected Mode)**: Sincronización con instancia central (si aplica)

### Acciones Previstas

- Ejecutar análisis tras completar cada fase de desarrollo
- Resolver todos los problemas críticos antes de merge
- Documentar justificaciones de problemas no resueltos

---

## Estrategia de Ramas y Pull Requests

### Modelo de Branching

Seguiremos un modelo modificado de Git Flow:

```
main (estable)
  ↓ (PR revisado)
develop (integración)
  ├── feature/validadores
  ├── feature/clasificacion
  ├── feature/metricas
  └── feature/pruebas
```

### Convenciones de Naming

- **Features**: `feature/nombre-descriptivo`
- **Bugfixes**: `bugfix/descripcion-del-error`
- **Documentación**: `docs/tema`
- **Testing**: `test/nombre-del-test`

### Proceso de Pull Request

1. Crear rama desde `develop`
2. Desarrollar e implementar funcionalidad
3. Crear PR contra `develop`
4. Ejecutar validaciones (tests, linting, análisis)
5. Revisión de código (mínimo 1 revisor)
6. Resolver comentarios
7. Merge a `develop`
8. Eventual release PR a `main`

### Criterios de Aceptación para PR

- ✅ Tests pasan (cobertura ≥ 80%)
- ✅ SonarQube: Sin problemas críticos
- ✅ Revisión de código aprobada
- ✅ Documentación actualizada
- ✅ Commits con mensajes claros (formato convencional)

---

## Consideraciones de Seguridad y Confidencialidad

### Principios de Seguridad

1. **Datos Ficticios Exclusivamente**: 
   - No utilizar información real de clientes, empleados o instituciones
   - No incorporar credenciales, contraseñas, tokens o APIs reales
   - No referenciar datos personales identificables (PII)

2. **Validación de Entrada**:
   - Validar y sanitizar todos los datos de entrada
   - Limitar longitudes de strings
   - Validar formatos de datos

3. **Gestión de Errores**:
   - No revelar información sensible en mensajes de error
   - Registrar errores sin comprometer confidencialidad
   - Implementar logging seguro

4. **Control de Acceso**:
   - Mantener código fuente en repositorio privado si es necesario
   - Documentar procedimientos de control de cambios

### Confidencialidad de Datos de Desarrollo

- 🚫 No incluir credenciales en archivos de configuración
- 🚫 No registrar datos sensibles en logs
- 🚫 No documentar información real de organizaciones
- ✅ Usar nombres ficticios consistentes (CLI-FIC-XXXX, AGENTE-XXX)
- ✅ Mantener trazabilidad de cambios mediante Git

---

## Cronograma Estimado

| Fase | Descripción | Duración Estimada |
|------|-------------|------------------|
| 1 | Definición y Planificación | 2-3 horas |
| 2 | Desarrollo Asistido | 4-5 horas |
| 3 | Datos Ficticios | 1-2 horas |
| 4 | Diseño de Casos de Prueba | 2-3 horas |
| 5 | Pruebas Unitarias e Integración | 3-4 horas |
| 6 | Análisis de Resultados | 1-2 horas |
| 7 | Corrección y Refactorización | 2-3 horas |
| 8 | Análisis SonarQube | 1-2 horas |
| 9-13 | Documentación, Git y Presentación | 3-4 horas |
| **Total** | | **20-30 horas** |

---

## Referencias y Recursos

- **Python Documentation**: https://docs.python.org/3/
- **pytest Documentation**: https://docs.pytest.org/
- **GitHub Copilot**: https://github.com/features/copilot
- **SonarQube**: https://www.sonarsource.com/

---

**Versión**: 1.0  
**Última actualización**: 2026-08-12  
**Estado**: Fase 1 - Planificación

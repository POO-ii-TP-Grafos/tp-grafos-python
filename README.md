# Sistema de Transporte Multimodal - TP Grafos

## Descripción del Problema

En una ciudad se diseñó un nuevo sistema de trasporte mediante una combinación de **hoverboard** y **tranvía**. 

### Componentes:
- **Nodos Principales**: Estaciones de tranvía
- **Nodos Secundarios**: Orígenes y destinos de pasajeros
- **Aristas de Hoverboard**: Transporte desde origen hasta estación y desde estación hasta destino
- **Aristas de Tranvía**: Red de transporte entre estaciones

### Fórmula de Costo:
```
Costo Total = K1 * kmHB + K2 * tramos

Donde:
- K1: Constante de costo por km en hoverboard
- K2: Constante de costo por tramo de tranvía
- kmHB: Distancia en km a recorrer en hoverboard
- tramos: Cantidad de estaciones de tranvía recorridas
```

## Problemas a Resolver

### 1. Rutas de Menor Costo para Pasajeros
Dado un par origen-destino, encontrar la ruta de menor costo.
- **Algoritmo**: Dijkstra (shortest path)
- Considera la combinación de hoverboard + tranvía

### 2. Ruta de Camioneta de Mantenimiento
Encontrar la ruta de menor costo para que la camioneta pase por todas las estaciones.
- **Algoritmo**: TSP (Traveling Salesperson Problem)
- Solo recorre nodos principales (estaciones)

## Estructura del Proyecto

```
├── src/
│   ├── otroNombre.py                    # Versión con gráficos (matplotlib)
│   └── otroNombre_sin_grafico.py        # Versión sin gráficos (para entornos virtuales)
├── tests/
│   ├── myTest.test.py                   # Tests antiguos
│   └── test_transporte.py               # Suite completa de tests con pytest
├── run_tests.py                         # Script para ejecutar pruebas manualmente
├── requirements.txt                     # Dependencias del proyecto
└── problem.md                           # Descripción del problema
```

## Instalación

### 1. Crear entorno virtual (si no existe):
```bash
python -m venv .venv
```

### 2. Activar entorno virtual:

**En Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**En Windows (CMD):**
```cmd
.venv\Scripts\activate.bat
```

**En Linux/Mac:**
```bash
source .venv/bin/activate
```

### 3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Ejecución de Pruebas

### Opción 1: Script Manual (Recomendado para entornos virtuales)
```bash
python run_tests.py
```

**Salida esperada:**
- Información de cada grafo
- 3+ pares origen-destino por grafo
- Rutas de menor costo con detalles
- Rutas de camioneta de mantenimiento (TSP)
- Estadísticas del grafo

### Opción 2: Pytest (Más detallado)
```bash
pytest tests/test_transporte.py -v
```

O para ver la salida de print:
```bash
pytest tests/test_transporte.py -v -s
```

### Opción 3: Con gráficos (matplotlib)
```bash
python -c "from tests.myTest.test import test_grafo_pequeno; test_grafo_pequeno()"
```

**Nota:** Esto solo funciona en entornos con GUI disponible.

## Grafos de Prueba

### Grafo 1: Pequeño (3 estaciones)
- **Nodos Principales**: E1, E2, E3
- **Nodos Secundarios**: O1, D1, O2, D2, O3, D3
- **Pares O-D**:
  1. O1 → D1 (ruta corta)
  2. O1 → D2 (cruza estaciones)
  3. O3 → D1 (ruta larga)

### Grafo 2: Grande (5 estaciones)
- **Nodos Principales**: Centro, Norte, Sur, Este, Oeste
- **Nodos Secundarios**: 8 nodos (casas y destinos)
- **Pares O-D**:
  1. Casa_A1 → Dest_A1 (ruta simple)
  2. Casa_A1 → Dest_D1 (ruta larga)
  3. Casa_B1 → Dest_C1 (ruta intermedia)
  4. Casa_D1 → Dest_B1 (otra ruta larga)

### Grafo 3: Anillo (4 estaciones en círculo)
- **Nodos Principales**: E_A, E_B, E_C, E_D
- **Nodos Secundarios**: Orig_1, Dest_1, Orig_2, Dest_2, Orig_3, Dest_3
- **Pares O-D**:
  1. Orig_1 → Dest_2 (tranvía A→B)
  2. Orig_2 → Dest_3 (tranvía B→C)
  3. Orig_1 → Dest_3 (ruta larga en anillo)

## Resultados de Pruebas

### Ejemplo de Salida

```
======================================================================
GRAFO: Grafo Pequeño
======================================================================
K1 (costo/km hoverboard) = $10
K2 (costo/tramo tranvía) = $20

======================================================================
1. RUTAS DE MENOR COSTO PARA PASAJEROS (Algoritmo Dijkstra)
======================================================================
  Origen: O1 | Destino: D1
    Ruta: O1 → E1 → D1
    Detalles: HB(2km, $20.0), HB(3km, $30.0)
    Costo Hoverboard: $50.00
    Costo Tranvía: $0.00
    ✓ COSTO TOTAL: $50.00

======================================================================
2. RUTA DE CAMIONETA DE MANTENIMIENTO (TSP)
======================================================================
  ✓ Ruta TSP (ciclo): E1 → E2 → E3 → E1
  Estaciones visitadas: 3
  ✓ COSTO TOTAL DEL CICLO: $120.00

======================================================================
3. ESTADÍSTICAS DEL GRAFO
======================================================================
  Total de nodos: 9
  Total de aristas: 9
  Nodos principales: 3
  Nodos secundarios: 6
  Aristas de hoverboard: 6
  Aristas de tranvía: 2
  Grafo conectado: True
```

## Librerías Utilizadas

- **networkx**: Manejo de grafos
  - `nx.shortest_path()` - Algoritmo de Dijkstra
  - `nx.traveling_salesperson_problem()` - TSP aproximado
  - `nx.is_connected()` - Verificación de conectividad

- **matplotlib**: Visualización de grafos (opcional)
  - Dibuja nodos y aristas con colores diferenciados
  - Etiquetas de pesos en aristas

- **pytest**: Testing (para suite de pruebas completa)

## Validación de la Solución

✅ **Problema 1**: Rutas de menor costo calculadas correctamente con Dijkstra
✅ **Problema 2**: Ruta de camioneta de mantenimiento calculada con TSP
✅ **Visualización**: Grafos mostrados con colores diferenciados (opcional)
✅ **Grafos**: 3 grafos distintos
✅ **Pruebas**: 3+ pares origen-destino por grafo (total 10 pares probados)

## Notas Técnicas

### Algoritmo de Dijkstra
- Encuentra el camino más corto entre dos nodos
- Tiempo: O((V + E) log V) con heap
- Garantiza el óptimo para grafos con pesos positivos

### Algoritmo TSP
- NetworkX usa `traveling_salesperson_problem()` que es una aproximación
- Devuelve un ciclo que visita todos los nodos
- No garantiza el óptimo pero es eficiente en tiempo polinomial

### Propiedades del Grafo
- **No dirigido**: Los viajes pueden ser en ambas direcciones
- **Pesos positivos**: Todos los costos son positivos
- **Conectado**: Existe camino entre cualquier par de nodos
- **Híbrido**: Combina dos tipos de aristas (hoverboard y tranvía)

## Troubleshooting

**Error: "No module named pytest"**
```bash
pip install pytest
```

**Error: "No module named networkx"**
```bash
pip install networkx
```

**Error: "No module named matplotlib"** (solo si usas versión con gráficos)
```bash
pip install matplotlib
```

**Error al mostrar gráficos en entorno virtual sin GUI:**
Usar `run_tests.py` o `otroNombre_sin_grafico.py` en su lugar.

## Autor
Implementación del TP Grafos - Programación con Objetos II (2026)

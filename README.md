
# Proyecto de Simulaciones Físicas

Este programa en Python permite realizar varias simulaciones y cálculos físicos relacionados con la caída libre, conversiones de velocidad, movimiento uniformemente acelerado (MUR), operaciones vectoriales, y lanzamientos de proyectiles. Se utiliza `matplotlib` para la visualización de los resultados y `numpy` para realizar cálculos y manipulación de arrays.

## Requisitos

Para ejecutar este programa, necesitas las siguientes librerías de Python:

- `math`: Funciones matemáticas básicas como raíces cuadradas y trigonometría.
- `numpy` (importada como `np`): Librería para trabajar con arrays y realizar operaciones numéricas avanzadas.
- `matplotlib.pyplot` (importada como `plt`): Se usa para generar gráficos y visualizaciones.

Para instalar las librerías `numpy` y `matplotlib`, usa el siguiente comando:

```bash
pip install numpy matplotlib
```

## Funciones del Programa

### `excersice_1(*highs)`
Simula la caída libre de un objeto desde varias alturas. Calcula el tiempo de caída y la velocidad final de cada altura dada y los grafica en una gráfica de altura contra tiempo. 

### `excersice_2(*duple)`
Convierte velocidades entre tres unidades: km/h, m/s y mph. Muestra una tabla de conversiones en forma visual.

### `excersice_3(*data)`
Calcula la velocidad final y el desplazamiento de un objeto bajo movimiento uniformemente acelerado (MUR) con un tiempo determinado. Muestra una tabla con los datos calculados.

### `excersice_4(vec_1, vec_2)`
Realiza la suma de dos vectores de la misma longitud y devuelve el resultado. 

### `excersice_5(vec_1, vec_2)`
Calcula el producto escalar entre dos vectores y el ángulo entre ellos. Los vectores deben tener la misma longitud.

### `excersice_6(v0, angle)`
Simula el lanzamiento de un proyectil con una velocidad inicial y un ángulo dado. Calcula el tiempo total de vuelo, la altura máxima y la distancia máxima alcanzada, y los visualiza en un gráfico de trayectoria.

## Uso del Programa

El programa incluye un menú interactivo que permite seleccionar la simulación que deseas realizar. Puedes ingresar los datos necesarios y ver los resultados tanto en formato numérico como en gráficos.

### Menú de opciones

1. Caída libre
2. Conversión de velocidades
3. Movimiento uniformemente acelerado (MUR)
4. Suma de vectores
5. Producto escalar entre dos vectores y ángulo
6. Lanzamiento de proyectiles

### Ejemplo de ejecución

En el menú, puedes ingresar los datos requeridos, como alturas para la caída libre o la velocidad inicial y el ángulo para el lanzamiento de proyectiles. Los resultados se muestran en gráficos y tablas, dependiendo de la opción seleccionada.

## Descripción de `matplotlib.pyplot` (`plt`)

`matplotlib.pyplot` se utiliza para generar gráficos y visualizaciones. Algunas de las funciones clave que se usan en este programa son:

- `plt.plot()`: Dibuja un gráfico de líneas o puntos.
- `plt.xlabel()`: Añade una etiqueta al eje X.
- `plt.ylabel()`: Añade una etiqueta al eje Y.
- `plt.title()`: Añade un título al gráfico.
- `plt.grid()`: Activa o desactiva la cuadrícula del gráfico.
- `plt.show()`: Muestra el gráfico en pantalla.
- `plt.text()`: Añade texto en posiciones específicas del gráfico.
- `plt.table()`: Muestra tablas con los datos calculados.
- `plt.arrow()`: Dibuja flechas en el gráfico (usado para representar vectores).

## Descripción de `numpy` (`np`)

`numpy` es una librería para el manejo eficiente de arrays y operaciones matemáticas avanzadas. Algunas funciones clave de `numpy` que se usan en este programa incluyen:

- `np.linspace()`: Genera una secuencia de números equidistantes entre dos valores (usado para generar puntos de tiempo en las simulaciones de trayectorias).
- `np.cos()`, `np.sin()`: Funciones trigonométricas usadas para calcular componentes de vectores en el lanzamiento de proyectiles.

## Ejecución del Programa

Para ejecutar el programa, simplemente ejecuta el archivo principal en un entorno de Python. Aparecerá un menú interactivo donde puedes seleccionar las simulaciones y cálculos que deseas realizar.

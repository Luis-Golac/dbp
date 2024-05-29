### 1. Definir el Modelo
El modelo dado es \( y = mx \). Nuestro objetivo es encontrar el parámetro \( m \) que minimiza el error cuadrático total.

### 2. Formular la Función de Error
El error cuadrático total está definido como:
\[ E_2 = \sum e_i^2 \]
donde \( e_i \) es el error de cada punto de datos y está dado por:
\[ e_i^2 = (mx_i - y_i)^2 \]

### 3. Calcular el Parámetro \( m \)
Para minimizar \( E_2 \), derivamos respecto a \( m \) y establecemos la derivada igual a cero:
\[ \frac{\partial E_2}{\partial m} = 2 \sum (mx_i - y_i)x_i = 0 \]

Esto se simplifica a:
\[ \sum x_i^2 \cdot m = \sum x_i y_i \]

Por lo tanto, el parámetro \( m \) está dado por:
\[ m = \frac{\sum x_i y_i}{\sum x_i^2} \]

### 4. Aplicar a los Datos
Dado el conjunto de datos:
\[ 
\begin{array}{cc}
X & Y \\
10100.25 & 317.86 \\
90841.96 & 2708.27 \\
267909.8 & 7916.96 \\
\end{array}
\]

Primero, calculamos \( \sum x_i y_i \) y \( \sum x_i^2 \):

\[
\sum x_i y_i = 10100.25 \cdot 317.86 + 90841.96 \cdot 2708.27 + 267909.8 \cdot 7916.96
\]

\[
\sum x_i^2 = 10100.25^2 + 90841.96^2 + 267909.8^2
\]

Ahora, realizamos los cálculos:

\[
\sum x_i y_i = 10100.25 \cdot 317.86 + 90841.96 \cdot 2708.27 + 267909.8 \cdot 7916.96 = 3211589.635 + 245924131.902 + 2120832212.408 = 2365877934.945
\]

\[
\sum x_i^2 = 10100.25^2 + 90841.96^2 + 267909.8^2 = 102015505.0625 + 8252177124.2416 + 71739825264 = 80022010993.3041
\]

Finalmente, calculamos \( m \):

\[
m = \frac{2365877934.945}{80022010993.3041} \approx 0.02957
\]

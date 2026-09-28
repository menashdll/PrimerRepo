# Explicación del método

La cuadratura de Gauss-Legendre aproxima una integral mediante

$$
\int_a^b f(x)\,dx \approx \sum_{i=1}^{N} w_i f(x_i).
$$

## Puntos y pesos

Para el intervalo estándar \([-1,1]\), los puntos de evaluacion corresponden a los ceros del polinomio de legendre. Considere los polinomios de legendre y defina el producto interno

$$<a|b> = \int_{-1}^1 a^*b \, dx$$

En este intervalo los polinomios de legendre son ortogonales con cualquier polinomio de grado menor al suyo. Ahora tome un polinomio de grado $2N-1$ y dividalo entre el polinomio de legendre. de aqui se obtiene.

$$p(x) = Q(x)P_N(x) + r(x)$$

note que se debe cumplir que el grado de $Q(x)$ es menor o igual a $N-1$ por ende

$$\int_{-1}^1 Q(x)P_N(x) \, dx = 0$$

Entonces

$$\int_{-1}^1 p(x) = \int_{-1}^1 r(x)$$

y cuando $P_N(x_i) = 0$ entonces $p(x_i) = r(x_i)$

Esto permite aproximar la integral de un polinomio $2N-1$ por un polinomio de grado $N-1$

De estos puntos de evaluacion se pueden obtener los pesos.

## Cambio de intervalo

Para trabajar en un intervalo general \([a,b]\), se utiliza

$$
x=\frac{b-a}{2}t+\frac{a+b}{2},
$$

por lo que los puntos y pesos se transforman como

$$
x_i'=\frac{b-a}{2}x_i+\frac{a+b}{2},
$$

$$
w_i'=\frac{b-a}{2}w_i.
$$

## Criterio de convergencia

Para funciones que no son polinomios, no existe una garantía de exactitud
para un número finito de puntos.

Por esta razón, la implementación incrementa \(N\) hasta cumplir

$$
|I_N-I_{N-1}|<\mathrm{tol}.
$$

## Aplicación al problema

En la tarea se aplica el método a

$$
f(x)=x^6-x^2\sin(2x)
$$

en el intervalo $[1,3]$.

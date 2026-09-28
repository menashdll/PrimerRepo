# Tutorial

Este módulo permite aproximar integrales definidas mediante cuadratura de Gauss-Legendre.

## Ejemplo de uso

Para resolver la integral de la tarea, primero se define el integrando y luego se utiliza `calcularIntegral`, indicando la función, los límites de integración y la tolerancia.

```python
import numpy as np

def funcEv(x):
    return x**6 - x**2 * np.sin(2*x)

resultado, N = calcularIntegral(funcEv, 1, 3, 1e-5)

print(resultado)
print(N)
```

# Mini Life Game

Implementación en Python del clásico Juego de la Vida de Conway.

## Uso

1. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```
2. Ejecuta el juego:
   ```
   python main.py
   ```

## Reglas del Juego

El juego se desarrolla en una cuadrícula donde cada celda tiene dos estados: viva o muerta. La evolución del juego depende del estado inicial de las celdas y de las siguientes reglas:

1. **Supervivencia**: Una celda viva con 2 o 3 vecinas vivas sobrevive a la siguiente generación.
2. **Muerte**: Una celda viva con menos de 2 vecinas vivas muere por soledad, y con más de 3 muere por sobrepoblación.
3. **Nacimiento**: Una celda muerta con exactamente 3 vecinas vivas se convierte en una celda viva.

## Ejemplo

Estado inicial:

```
. . . . .
. * * * .
. . * . .
. * * * .
. . . . .
```

Después de aplicar las reglas del juego, el siguiente estado será:

```
. . . . .
. . * . .
. * * * .
. . * . .
. . . . .
```

## Características

- Configuración de tamaño de tablero, turnos y tiempo entre turnos.
- Inserción manual de células vivas.
- Visualización clara en consola.

## Créditos

Este juego fue creado como un proyecto personal para aprender más sobre programación en Python y sobre el concepto de autómatas celulares. Agradecimientos especiales a John Conway por su contribución a la matemática y la teoría de juegos.

## Licencia

MIT License
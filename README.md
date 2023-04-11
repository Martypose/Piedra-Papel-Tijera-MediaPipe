# Juego de Piedra, Papel, Tijeras con MediaPipe

Este proyecto es una implementación del clásico juego de Piedra, Papel, Tijeras utilizando el reconocimiento de gestos con MediaPipe.

## Cómo funciona

El juego utiliza la solución de reconocimiento de manos de MediaPipe para detectar y reconocer los gestos de Piedra, Papel y Tijeras realizados por el usuario.

### Proceso de juego

1. Ejecuta el programa. Verás una ventana mostrando la cámara en tiempo real.
2. Haz doble clic en la ventana de la cámara para iniciar la cuenta atrás.
3. La cuenta atrás comenzará con un mensaje de "Empezamos" y luego mostrará las palabras "piedra", "papel" y "tijera" en orden antes de mostrar "YA!".
4. Cuando aparezca "YA!", realiza un gesto de Piedra, Papel o Tijeras con tu mano frente a la cámara.
5. Una vez que el usuario ha mostrado su jugada, el programa generará aleatoriamente una jugada para la máquina.
6. Se comparan las jugadas del usuario y la máquina, y se muestra el resultado en la ventana de la cámara (GANA EL JUGADOR, GANA LA MÁQUINA o EMPATE).

## Dependencias

- Python 3
- OpenCV
- MediaPipe
- TensorFlow

## Créditos

Este proyecto utiliza la solución de reconocimiento de manos de [MediaPipe](https://github.com/google/mediapipe) y el modelo de aprendizaje profundo entrenado con TensorFlow para la clasificación de gestos.

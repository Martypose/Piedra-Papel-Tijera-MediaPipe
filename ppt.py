import time
import random
import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

f = open("gesture.names", "r")
classNames = f.read().split("\n")
f.close()

model = load_model("mp_hand_gesture")

cuenta_atras = ["Empezamos", "piedra", "papel", "tijera", "YA!"]

posibles_jugadas = ["piedra", "papel", "tijera"]


indiceCuenta = 0

texto = ""
jugadadelpc = ""
jugadaplayer = ""
jugadaplayerfinal = ""
tiempo = 0
tiempoJugar = 0


def click_raton(event, x, y, flags, param):
    global texto
    global tiempo
    if event == cv2.EVENT_LBUTTONDBLCLK:
        # obtener el tiempo actual al hacer click
        tiempo = time.time()
        print("click")
        print(tiempo)
        texto = cuenta_atras[indiceCuenta]


vid = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.namedWindow("Objeto")
cv2.setMouseCallback("Objeto", click_raton)

while True:
    ret, img_bgr = vid.read()
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    img_rgb.flags.writeable = False
    x, y, z = img_bgr.shape
    result = hands.process(img_rgb)
    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                lmx = int(lm.x * x)
                lmy = int(lm.y * y)
                landmarks.append([lmx, lmy])
            mpDraw.draw_landmarks(img_bgr, handslms, mpHands.HAND_CONNECTIONS)
            prediccion = model.predict([landmarks])
            # print(prediccion)
            indice = np.argmax(prediccion)
            nombre = classNames[indice]
            if nombre == "peace":
                nombre = "tijera"
            elif nombre == "fist":
                nombre = "piedra"
            elif nombre == "stop":
                nombre = "papel"
            else:
                nombre = "INVALIDA"

            jugadaplayer = nombre

    img_bgr = cv2.flip(img_bgr, 1)

# termino la cuenta atras, la maquina elige una jugada
    if int(time.time()) - int(tiempo) > 1 and texto != "" and indiceCuenta < 5:
        texto = cuenta_atras[indiceCuenta]
        indiceCuenta += 1
        tiempo = time.time()
        if indiceCuenta > 4:
            texto = "YA!"
            tiempoJugar = time.time()
            
            



    if jugadadelpc == "" and jugadaplayer != "" and jugadaplayer != "INVALIDA" and texto == "YA!":
    # si termino la cuenta atras, espero a que el usuario haga la señal y comparo las señales
        jugadadelpc = posibles_jugadas[random.randint(0, 2)]

        # lo que tenga el jugador en mano pasado un segundo se queda como su jugada final
        jugadaplayerfinal = jugadaplayer
        if jugadadelpc == jugadaplayerfinal:
            texto = "EMPATE"
        elif jugadadelpc == "piedra" and jugadaplayerfinal == "tijera":
            texto = "GANA LA MAQUINA"
        elif jugadadelpc == "papel" and jugadaplayerfinal == "piedra":
            texto = "GANA LA MAQUINA"
        elif jugadadelpc == "tijera" and jugadaplayerfinal == "papel":
            texto = "GANA LA MAQUINA"
        else:
            texto = "GANA EL JUGADOR"

    cv2.putText(
        img_bgr,
        "Maquina: " + jugadadelpc,
        (50, 350),
        font,
        1,
        (0, 255, 255),
        2,
        cv2.LINE_4,
    )
    cv2.putText(
        img_bgr,
        "Humano: " + jugadaplayerfinal,
        (400, 350),
        font,
        1,
        (0, 255, 255),
        2,
        cv2.LINE_4,
    )
    cv2.putText(img_bgr, texto, (50, 50), font, 1, (0, 255, 255), 2, cv2.LINE_4)

    cv2.putText(img_bgr, jugadaplayer, (400, 50), font, 1, (0, 255, 255), 2, cv2.LINE_4)

    cv2.imshow("Objeto", img_bgr)
    if cv2.waitKey(10) & 0xFF == 27:
        break

vid.release()

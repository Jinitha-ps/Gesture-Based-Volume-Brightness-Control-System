import cv2
import time
import numpy as np
import math
import HandTrackingModule1 as htm
import screen_brightness_control as sbc

from pycaw.pycaw import AudioUtilities


# ---------------- CAMERA SETTINGS ----------------
wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(detectionCon=0.7)


# ---------------- VOLUME SETUP ----------------
devices = AudioUtilities.GetSpeakers()
volume = devices.EndpointVolume

volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]

# ---------------- VARIABLES ----------------
volBar = 400
volPer = 0
brightBar = 400
brightPer = 0
pTime = 0


while True:
    success, frame = cap.read()
    img = detector.findHands(frame)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:

        # ================= VOLUME CONTROL =================
        # Thumb tip = 4
        # Index tip = 8
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]

        length = math.hypot(x2 - x1, y2 - y1)

        vol = np.interp(length, [50, 300], [minVol, maxVol])
        volBar = np.interp(length, [50, 300], [400, 150])
        volPer = np.interp(length, [50, 300], [0, 100])

        volume.SetMasterVolumeLevel(vol, None)

        cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 2)

        # ================= BRIGHTNESS CONTROL =================
        # Middle finger tip = 12
        x3, y3 = lmList[12][1], lmList[12][2]

        length2 = math.hypot(x3 - x1, y3 - y1)

        bright = np.interp(length2, [50, 300], [0, 100])
        brightBar = np.interp(length2, [50, 300], [400, 150])
        brightPer = np.interp(length2, [50, 300], [0, 100])

        sbc.set_brightness(int(bright))

        cv2.circle(img, (x3, y3), 10, (0, 255, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x3, y3), (0, 255, 255), 2)

    # ================= VOLUME BAR =================
    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 2)
    cv2.rectangle(img, (50, int(volBar)), (85, 400),
                  (255, 0, 0), cv2.FILLED)
    cv2.putText(img, f'Vol: {int(volPer)}%', (40, 430),
                cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 0, 0), 2)

    # ================= BRIGHTNESS BAR =================
    cv2.rectangle(img, (550, 150), (585, 400), (0, 255, 255), 2)
    cv2.rectangle(img, (550, int(brightBar)), (585, 400),
                  (0, 255, 255), cv2.FILLED)
    cv2.putText(img, f'Bright: {int(brightPer)}%', (440, 430),
                cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 255), 2)

    # ================= FPS =================
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (20, 50),
                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)

    cv2.imshow("Gesture Volume & Brightness Control", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
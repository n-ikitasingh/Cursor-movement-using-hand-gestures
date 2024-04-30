E:\Python\HandGesture\2hands\combine2.py
import cv2
import numpy as np
import handtracking1 as htm
import time
import autopy
import pyautogui

##########################
wCam, hCam = 640, 480
frameR = 100  # Frame Reduction
smoothening = 10
#########################

# Get screen size
wScr, hScr = autopy.screen.size()

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.HandDetector(maxHands=1)

pyautogui.FAILSAFE = False

while True:
    # 1. Find hand Landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    fingers = detector.fingersUp()

    # 2. Get the tip of the index and middle fingers
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

    # 3. Check gesture mode
    if fingers == [0, 0, 0, 0, 0]:
        mode = 'N'
    elif fingers == [0, 1, 0, 0, 0] or fingers == [0, 1, 1, 0, 0]:
        mode = 'Scroll'
    elif fingers == [1, 1, 0, 0, 0]:
        mode = 'Volume'
    elif fingers == [1, 1, 1, 1, 1]:
        mode = 'Cursor'

    # 4. Gesture Actions
    if mode == 'Scroll':
        cv2.rectangle(img, (200, 410), (245, 460), (255, 255, 255), cv2.FILLED)
        if fingers == [0, 1, 0, 0, 0]:
            pyautogui.scroll(300)
        elif fingers == [0, 1, 1, 0, 0]:
            pyautogui.scroll(-300)
    elif mode == 'Cursor':
        x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
        y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
        clocX = plocX + (x3 - plocX) / smoothening
        clocY = plocY + (y3 - plocY) / smoothening
        autopy.mouse.move(wScr - clocX, clocY)
        plocX, plocY = clocX, clocY

        # Left Click
        if fingers[0] == 0:
            autopy.mouse.click()

        # Right Click
        if fingers[-1] == 0:  # Check if pinky finger is down
            autopy.mouse.click(button=autopy.mouse.Button.RIGHT)

    # Display FPS and image
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
   # cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("Hand LiveFeed", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

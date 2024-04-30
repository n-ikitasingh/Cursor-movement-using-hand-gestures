import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)  # Detect multiple hands

    if hands:
        for hand in hands:
            lmList = hand["lmList"]  # List of 21 Landmarks points
            bbox = hand["bbox"]  # Bounding Box info x,y,w,h
            centerPoint = hand["center"]  # center of the hand cx,cy
            handType = hand["type"]  # Hand Type Left or Right

            fingers = detector.fingersUp(hand)
            # Perform text editing actions based on finger states or gestures

        if len(hands) == 2:
            hand1, hand2 = hands[0], hands[1]
            lmList1, lmList2 = hand1["lmList"], hand2["lmList"]
            bbox1, bbox2 = hand1["bbox"], hand2["bbox"]
            centerPoint1, centerPoint2 = hand1["center"], hand2["center"]
            handType1, handType2 = hand1["type"], hand2["type"]

            fingers1, fingers2 = detector.fingersUp(hand1), detector.fingersUp(hand2)
            # Perform text editing actions based on finger states or gestures between two hands
            # Implement gestures or interactions between multiple hands if required

            # Visualize hand interactions or relationships between multiple hands, if applicable

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

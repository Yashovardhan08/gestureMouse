import cv2
import mediapipe as mp
import time


cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
prevTime = 0
currTime = 0
while True:
    success,img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
    # print(results.multi_hand_landmarks)
    currTime = time.time()
    fps = 1/(currTime-prevTime)
    prevTime = currTime

    cv2.putText(img,str(fps),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),2)

    cv2.imshow("Image",img)
    cv2.waitKey(1)

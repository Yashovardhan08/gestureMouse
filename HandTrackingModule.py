import cv2
import mediapipe as mp
import time
import DetectClick
import MouseControls
import threading


class HandDetector:
    def __init__(self, mode=False,maxHands=2,detectionCon=0.5,trackCon=0.5):
        self.c = None
        self.w = None
        self.results = None
        self.h = None
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,1,self.detectionCon,self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self,img,flag=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.h, self.w, self.c = img.shape
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks and flag:
            for handLms in self.results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, handNumber=0):
        lmList = []
        if self.results.multi_hand_landmarks:
            handLms = self.results.multi_hand_landmarks[handNumber]
            for id, lm in enumerate(handLms.landmark):
                cx = 1-lm.x
                cy = lm.y
                lmList.append([cx,cy])
        return lmList


def processClick(clickDetector,landmark_list,mouseController, fps):
    click = clickDetector.update(landmark_list,mouseController,fps)
    if click == "double":
        mouseController.double_click()
    elif click == "left":
        mouseController.left_click()
    elif click == "right":
        mouseController.right_click()


def main():
    prevTime = 0
    cap = cv2.VideoCapture(0)
    # cap.set(cv2.CAP_PROP_FPS,25)
    SCREEN = 110
    cap.set(3, 16*SCREEN)
    cap.set(4, 10*SCREEN)
    mouseController = MouseControls.MouseController(16*SCREEN,10*SCREEN)
    handDetect = HandDetector()
    lock = threading.Lock()
    clickHandler = DetectClick.DetectClicks(mouseController,lock)
    thread = threading.Thread(target=clickHandler.run_detections)
    thread.start()
    while True:
        success,img = cap.read()
        currTime = time.time()
        fps = 1 / (currTime - prevTime)
        prevTime = currTime
        img = handDetect.findHands(img,True)
        landmarks = handDetect.findPosition(0)
        lock.acquire()
        clickHandler.push_landmark(landmarks)
        lock.release()
        # if thread.is_alive() is False
        # if len(landmark_list)>0 :
        #     print( "Index base is at :" + str(landmark_list[5]))
        # processClick(clickDetector,landmark_list,mouseController,fps)

        # click = clickHandler.update(landmarks,mouseController,fps)
        # if click == "double":
        #     mouseController.double_click()
        # elif click == "left":
        #     mouseController.left_click()
        # elif click == "right":
        #     mouseController.right_click()

        cv2.putText(img, str(fps), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 2)
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__  == "__main__":
    main()

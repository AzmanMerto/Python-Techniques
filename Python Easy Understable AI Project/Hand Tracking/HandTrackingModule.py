import  cv2
import mediapipe as mp
import time

class handDetector():

    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5 ):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        # Capturing Hands
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=mode,
                                        max_num_hands=maxHands,
                                        min_detection_confidence=detectionCon,
                                        min_tracking_confidence=trackCon)
        self.mpDraw = mp.solutions.drawing_utils


    def findHands(self, img, draw=True):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(imgRGB)

        # hands color
        blue_color = (255, 0, 0)
        drawing_spec = self.mpDraw.DrawingSpec(color=blue_color, thickness=2, circle_radius=2)


        if self.result.multi_hand_landmarks:
            for handLms in self.result.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS,
                                      landmark_drawing_spec = drawing_spec,
                                      connection_drawing_spec = drawing_spec)

        return img

    def findPosition(self, img, handNo = 0, draw = True ):

        lmList = []
        if self.result.multi_hand_landmarks:
            myHand = self.result.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        return lmList

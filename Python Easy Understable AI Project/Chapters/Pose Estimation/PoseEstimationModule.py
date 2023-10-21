import cv2
import mediapipe as mp
import time

class PossDetector():

    def __init__(self,mode=False, detection=0.5, tracking=0.5):
        self.mode = mode
        self.detection = detection
        self.tracking = tracking

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(static_image_mode=mode,
                                     min_detection_confidence=detection,
                                     min_tracking_confidence=tracking)

    def findPose(self,img,draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = self.pose.process(imgRGB)
        landmarks = result.pose_landmarks
        if draw:
            if landmarks:
                self.mpDraw.draw_landmarks(img, landmarks,self.mpPose.POSE_CONNECTIONS)
                for id, lm in enumerate(landmarks.landmark):
                    h,w,c = img.shape

                    cx, cy = int(lm.x * w), int(lm.y * h)
                    cv2.circle(img, (cx,cy), 5, (255,0,0), cv2.FILLED)


def main():
    capture = cv2.VideoCapture(0)
    pTime = 0

    detector = PossDetector()
    while True:
        success, img = capture.read()
        detector.findPose(img)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (30, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 3)
        cv2.imshow("image", img)
        cv2.waitKey(2)


if __name__ == "__main__":
    main()
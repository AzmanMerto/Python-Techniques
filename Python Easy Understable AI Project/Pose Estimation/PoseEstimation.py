import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

capture = cv2.VideoCapture(0)
pTime = 0

while True:
    success, img = capture.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = pose.process(imgRGB)

    landmarks = result.pose_landmarks

    if landmarks:
        mpDraw.draw_landmarks(img, landmarks)
        for id, lm in enumerate(landmarks.landmark):
            h,w,c = img.shape

            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(img, (cx,cy), 5, (255,0,0), cv2.FILLED)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)),(30,70),cv2.FONT_HERSHEY_COMPLEX, 3,(255,0,0), 3)

    cv2.imshow("image",img)
    cv2.waitKey(2)
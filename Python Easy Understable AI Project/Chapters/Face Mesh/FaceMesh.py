import cv2
import mediapipe as mp
import time

capture = cv2.VideoCapture(0)

mpFaceMesh = mp.solutions.face_mesh
mpDrawing = mp.solutions.drawing_utils
faceMash = mpFaceMesh.FaceMesh()

pTime = 0
while True:
    success,img = capture.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = faceMash.process(imgRGB)
    result = results.multi_face_landmarks

    if result:
        for faceLms in result:
            mpDrawing.draw_landmarks(img,faceLms,mpFaceMesh.FACEMESH_CONTOURS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img,f"fps: {int(fps)}",(30,70),cv2.FONT_HERSHEY_COMPLEX ,2, (255,0,255),1)

    cv2.imshow("Face Mesh", img)
    cv2.waitKey(1)


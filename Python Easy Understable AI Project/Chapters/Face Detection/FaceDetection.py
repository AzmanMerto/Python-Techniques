import cv2
import mediapipe as mp
import time

capture = cv2.VideoCapture(0)
pTime = 0

mpFaceDetection = mp.solutions.face_detection
mpDrawing = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection()

while True:
    success,img = capture.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)
    result = results.detections

    if result:
        for id, detection in enumerate(result):
            mpDrawing.draw_detection(img,detection)
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(img,bbox,(255,0,255),1)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img,f'FPS:{int(fps)}',(20,70), cv2.FONT_HERSHEY_COMPLEX, 2,(230,0,0),3)
    cv2.imshow("Face Detection", img)
    cv2.waitKey(1)
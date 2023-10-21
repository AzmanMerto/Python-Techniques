import  cv2
import time
import HandTrackingHelper
import HandTrackingModule


def main():
    # Using webcam
    capture = cv2.VideoCapture(0)

    # Set FPS
    pTime = 0
    cTime = 0

    detector = HandTrackingModule.handDetector()
    while True:
        success, img = capture.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)

        HandTrackingHelper.checkSuccess(success)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 0), 3)

        cv2.flip(img, 1)
        cv2.imshow("Hand Tracking", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
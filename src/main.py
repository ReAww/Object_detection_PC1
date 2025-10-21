import cv2
from detector import ObjectDetector

def main():
    detector = ObjectDetector()
    cap = cv2.VideoCapture(0)  # gunakan kamera laptop

    print("Tekan 'q' untuk keluar")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = detector.detect(frame)
        cv2.imshow("YOLO Real-Time Detector", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
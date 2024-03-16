
import cv2
from ultralytics import YOLO
model = YOLO("D:\\Dev_Vision\\ARM_ROBOT\\runs\\detect\\train2\\\weights\\best.pt")

cap = cv2.VideoCapture("D:\\Dev_Vision\\Project\\all.mp4")
#cap = cv2.VideoCapture(1)

while cap.isOpened():
    success, frame = cap.read()
    if success:
        results = model(frame)
        annotated_frame = results[0].plot()
        cv2.imshow("YOLOv8 Inference", annotated_frame)
        for result in results:
            print("class", result.boxes.cls)
            print("xyxy", result.boxes.xyxy)
            print("conf", result.boxes.conf)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()

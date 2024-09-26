import cv2
from ultralytics import YOLO
# Load the YOLOv8 model
model = YOLO("D:\\Dev_Vision\\YoLo_8\\runs\detect\\train11\\weights\\best.pt")
# Open the image file
image = cv2.imread('frame398.jpg')
# Loop through the image
results = model(image)
# Visualize the results on the image
annotated_image = results[0].plot()
# Display the annotated image
cv2.imshow("YOLOv8 Inference", annotated_image)
for result in results:
    print("class", result.boxes.cls)
    print("xyxy", result.boxes.xyxy)
    print("conf", result.boxes.conf)
cv2.waitKey(0)
cv2.destroyAllWindows()
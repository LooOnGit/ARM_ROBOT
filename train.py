from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.pt')
# model = YOLO('yolo8tiny2.yaml')
# model = YOLO("D:\\Dev_Vision\\Project\\runs\detect\\train\\weights\\last.pt")

if __name__ == '__main__': # can khi chay bang GPU
    model.train(data='dataset.yaml',epochs=50,imgsz=640,batch=3,optimizer='SGD')
    metrics = model.val()
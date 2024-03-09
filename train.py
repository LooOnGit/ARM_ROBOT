from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.pt')
# model = YOLO("D:\\Dev_Vision\\Project\\runs\detect\\train\\weights\\last.pt")

if __name__ == '__main__': # can khi chay bang GPU
    model.train(data='dataset.yaml',epochs=20,imgsz=640,batch=24,optimizer='Adam')
    metrics = model.val()
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # Or yolov8s.pt for more accuracy
model.train(data="dataset.yaml", epochs=20, imgsz=640, batch=8)

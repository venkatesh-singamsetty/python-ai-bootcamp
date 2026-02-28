from ultralytics import YOLO

# Load a YOLO model (yolo11n.pt will be downloaded automatically if not present)
model = YOLO("yolo11n.pt", "v11")

# Run prediction
# save=True will save the detection image to 'runs/detect/predict/'
detection_output = model.predict(
    source='https://c8.alamy.com/comp/R92782/handsome-young-man-working-on-laptop-while-enjoying-coffee-in-cafe-R92782.jpg', 
    conf=0.25,
    save=True
)

#print(detection_output)

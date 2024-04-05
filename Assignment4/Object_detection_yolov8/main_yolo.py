from ultralytics import YOLO
import cv2
import numpy as np 
from fastapi import FastAPI,File,Form,UploadFile,HTTPException
from fastapi.responses import StreamingResponse
import io
import json


app = FastAPI()
model = YOLO("yolov8n.pt")

@app.get("/")
def read_root():
    mes = "Welcome to object detection with YOLO v8"
    return mes

@app.post("/detection")
async def object_detection(input_file: UploadFile = File(None)):
    if not input_file.content_type.startswith("image/"):
        raise HTTPException(415,detail="Unsupported file type")
    
    contents = await input_file.read()
    np_array = np.frombuffer(contents,dtype=np.uint8)
    image = cv2.imdecode(np_array,cv2.IMREAD_UNCHANGED)
    cv2.imwrite("test.jpg",image)

    results = model(image)
    boxes = results[0].boxes.xyxy.tolist()
    clss = results[0].boxes.cls.tolist()
    names = results[0].names
    confs = results[0].boxes.conf.tolist()

    ultralytics_json = []
    for box, cls, conf in zip(boxes, clss, confs):
        x1, x2, y1, y2 = box
        x1 = int(x1)
        x2 = int(y1)
        y1 = int(x2)
        y2 = int(y2)
        conf = str(int(conf * 100))+"%"
        name = names[int(cls)]

        box_data = {
            "name": name,
            "class": int(cls),
            "confidence": conf,
            "box": {
                "x1": x1,
                "x2": x2,
                "y1": y1,
                "y2": y2,
            }
        }

        ultralytics_json.append(box_data)
    return ultralytics_json

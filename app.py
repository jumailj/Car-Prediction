from fastapi import FastAPI, File, UploadFile
from ultralytics import YOLO
from PIL import Image
import io

# Initialize FastAPI app
app = FastAPI()

# Load YOLO model (ensure best.pt is in the same directory)
MODEL_PATH = "best.pt" 
model = YOLO(MODEL_PATH)

# Define endpoint
@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Read image from request
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))

    # Run inference
    results = model(image)

    # Check if detection is successful

    print(results)
    if results:
        # Extract class name, class ID, and confidence from the first detected object
        # YOLO returns 'results' as a list, with each result containing a class and score
        predictions = []

        # Iterate over all detected objects (bounding boxes)
        for result in results[0].boxes:
            print(result)
            # Extract class ID, class name, and confidence score
            predicted_class_id = int(result.cls)  # Class ID
            predicted_class = results[0].names[predicted_class_id]  # Class name
            confidence = result.conf[0].item()  # Confidence score

            predictions.append({
                "class_label": predicted_class,
                "class_id": predicted_class_id,
                "confidence": confidence
            })

        return {
            "prediction": predictions,
            "message": "Image successfully classified"
        }
        
    
    return {"error": "No predictions made by the model"}

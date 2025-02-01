import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2
import pandas as pd  # Import for tabular display

# Streamlit UI
st.title("Multi-Class Vehicle Classication for Online Auto Marketplac")
st.write("Upload an image to predict objects.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
    
    # Convert the uploaded image to a PIL image
    image = Image.open(uploaded_file).convert("RGB")

    # Load YOLO model (Make sure "last.pt" exists)
    model = YOLO("last.pt")

    # Run inference
    results = model.predict(image)

    # Get first result
    result = results[0]

    if len(result.boxes) > 0:  # Check if any objects are detected
        # Convert image to OpenCV format for drawing
        img_np = np.array(image)
        img_cv = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

        predictions = []  # List to store predictions

        # Extract class names, IDs, and confidence scores
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates
            confidence = box.conf[0].item()  # Confidence score
            class_id = int(box.cls)  # Class ID
            class_name = result.names[class_id]  # Class name

            # Draw bounding box and label
            cv2.rectangle(img_cv, (x1, y1), (x2, y2), (0, 255, 0), 2)
            label = f"{class_name} ({confidence:.2f})"
            cv2.putText(img_cv, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Append prediction to list
            predictions.append({
                "Class": class_name,
                "Confidence": f"{confidence:.2f}"
            })

        # Convert back to RGB format for Streamlit
        img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)

        # Display image with bounding boxes
        st.image(img_rgb, caption="Predicted Image", use_container_width=True)

        # Show predictions as a table
        if predictions:
            st.write("Predictions:")
            st.table(pd.DataFrame(predictions))  # Display as table

    else:
        st.write("No objects detected.")

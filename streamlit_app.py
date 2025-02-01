import streamlit as st
from ultralytics import YOLO
from PIL import Image
import io

# Streamlit UI
st.title("YOLO Object Detection")
st.write("Upload an image to predict objects.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    
    # Convert the uploaded image to a PIL image
    image = Image.open(uploaded_file)

    # Load YOLO model (make sure you have your `last.pt` model in the correct path)
    model = YOLO("last.pt")  # Change this to your actual model path
    
    # Run inference
    results = model(image)

    # Check if detection is successful
    if results:
        # Display the image with the bounding boxes drawn on detected objects
        st.image(results[0].plot(), caption="Predicted Image", use_column_width=True)

        # Extract class names, IDs, and confidence scores
        predictions = []
        for result in results[0].boxes:
            predicted_class_id = int(result.cls)  # Class ID
            predicted_class = results[0].names[predicted_class_id]  # Class name
            confidence = result.conf[0].item()  # Confidence score

            predictions.append({
                "class_label": predicted_class,
                "class_id": predicted_class_id,
                "confidence": confidence
            })
        
        # Display predictions
        st.write("Predictions:")
        for prediction in predictions:
            st.write(f"Class: {prediction['class_label']}")
            st.write(f"Class ID: {prediction['class_id']}")
            st.write(f"Confidence: {prediction['confidence']:.2f}")
    else:
        st.write("No objects detected.")
